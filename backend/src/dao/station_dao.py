from business_object.station import Station
from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log

logger = get_logger(__name__)


class StationDao:

    @log
    def create(self, station: Station) -> bool:
        """ Crée une station dans la base de données
        Args:
            station: La station à mettre dans le base de données
        Returns:
            bool: True si la création a bien été faite, False sinon
        """
        res = None

        try:
            with DBConnection.connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO station(nom, code) VALUES"
                        "(%(nom)s, %(code)s"
                        "RETURNING id;",
                        {
                            "nom": station.nom,
                            "code": station.code,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        cree = False
        if res:
            station.id = res["id"]
            cree = True

        return cree

    @log
    def find_by_id(self, id: int) -> Station:
        """Trouve une station à partir de son id
        Args:
            id (int): L'ID de la station
        Returns:
            Station qui correspond à l'id donné
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                       "
                        "FROM station                   "
                        "WHERE id = %(id)s;             ",
                        {"id": id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        line = None
        if res:
            line = Station(
                id=res["id"],
                nom=res["nom"],
                code=res["code"],
            )
        return line

    @log
    def update(self, station) -> bool:
        """Update une station dans la base de données
        Args:
            station (Station): la station qui doit être actualisée
        Returns:
            True si actualisée, False sinon
        """
        nb_rows = 0

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE station             "
                        "   SET nom = %(nom)s,   "
                        ""
                        "WHERE id = %(id)s;      ",
                        {
                            "id": line.id,
                            "nom": line.nom,
                        },
                    )
                    nb_rows = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise
        return nb_rows == 1

    @log
    def delete(self, line) -> bool:
        """Supprime une ligne de la base de données
        Args:
            line (Line): la réservation à supprimer
        Returns:
            True si la réservation a été supprimée, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM line "
                        "WHERE id = %(id)s   ",
                        {"id": line.id},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise
        return res > 0
