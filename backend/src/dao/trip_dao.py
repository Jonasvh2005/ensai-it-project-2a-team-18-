from business_object.trip import Trip
from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log

logger = get_logger(__name__)


class TripDao:

    @staticmethod
    def _from_row(row) -> Trip:
        return Trip(
            id=row["id_trip"],
            dep_station_id=row["dep_station_id"],
            arr_station_id=row["arr_station_id"],
            dep_datetime=row["dep_datetime"],
            arr_datetime=row["arr_datetime"],
            statut=row["statut"],
            creator_id=row["creator_id"],
        )

    @log
    def create(self, trip: Trip) -> bool:
        """Crée un trajet dans la base de données
        Args:
            trip: Le trajet à mettre dans la base de données
        Returns:
            bool: True si la création a bien été faite, False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO trip(dep_station_id, arr_station_id, dep_datetime, "
                        "                 arr_datetime, statut, creator_id) VALUES "
                        "(%(dep_station_id)s, %(arr_station_id)s, %(dep_datetime)s, "
                        " %(arr_datetime)s, %(statut)s, %(creator_id)s) "
                        "RETURNING id_trip;",
                        {
                            "dep_station_id": trip.dep_station_id,
                            "arr_station_id": trip.arr_station_id,
                            "dep_datetime": trip.dep_datetime,
                            "arr_datetime": trip.arr_datetime,
                            "statut": trip.statut,
                            "creator_id": trip.creator_id,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        cree = False
        if res:
            trip.id = res["id_trip"]
            cree = True

        return cree

    @log
    def find_by_id(self, id: int) -> Trip:
        """Trouve un trajet à partir de son id
        Args:
            id (int): L'ID du trajet
        Returns:
            Trip qui correspond à l'id donné (None si introuvable)
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM trip WHERE id_trip = %(id)s;",
                        {"id": id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        return self._from_row(res) if res else None

    @log
    def find_by_stations(self, dep_station_id: int, arr_station_id: int) -> list[Trip]:
        """Trouve les trajets entre deux gares (recherche F4), du plus proche au plus lointain
        Args:
            dep_station_id (int): id de la gare de départ
            arr_station_id (int): id de la gare d'arrivée
        Returns:
            list[Trip]: la liste des trajets correspondants
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM trip "
                        "WHERE dep_station_id = %(dep)s AND arr_station_id = %(arr)s "
                        "ORDER BY dep_datetime;",
                        {"dep": dep_station_id, "arr": arr_station_id},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logger.error(e)
            raise

        return [self._from_row(row) for row in res]

    @log
    def update(self, trip: Trip) -> bool:
        """Met à jour un trajet dans la base de données
        Args:
            trip (Trip): le trajet qui doit être actualisé
        Returns:
            True si actualisé, False sinon
        """
        nb_rows = 0

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE trip "
                        "   SET dep_station_id = %(dep_station_id)s, "
                        "       arr_station_id = %(arr_station_id)s, "
                        "       dep_datetime = %(dep_datetime)s, "
                        "       arr_datetime = %(arr_datetime)s, "
                        "       statut = %(statut)s, "
                        "       creator_id = %(creator_id)s "
                        "WHERE id_trip = %(id)s;",
                        {
                            "id": trip.id,
                            "dep_station_id": trip.dep_station_id,
                            "arr_station_id": trip.arr_station_id,
                            "dep_datetime": trip.dep_datetime,
                            "arr_datetime": trip.arr_datetime,
                            "statut": trip.statut,
                            "creator_id": trip.creator_id,
                        },
                    )
                    nb_rows = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise
        return nb_rows == 1

    @log
    def delete(self, trip: Trip) -> bool:
        """Supprime un trajet de la base de données
        Args:
            trip (Trip): le trajet à supprimer
        Returns:
            True si le trajet a été supprimé, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM trip WHERE id_trip = %(id)s;",
                        {"id": trip.id},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise
        return res > 0
