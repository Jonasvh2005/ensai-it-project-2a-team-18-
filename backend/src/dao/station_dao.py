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
                        "INSERT INTO station(sncf_id, nom, ville, latitude, longitude) VALUES"
                        "(%(sncf_id)s, %(nom)s, %(ville)s, %(latitude)s, %(longitude)s)"
                        "RETURNING id;",
                        {
                            "sncf_id": station.sncf_id,
                            "nom": station.nom,
                            "ville": station.ville,
                            "latitude": station.latitude,
                            "longitude": station.longitude,
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
                sncf_id=res["sncf_id"],
                ville=res["ville"],
                latitude=res["latitude"],
                longitude=res["longitude"]
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
                        "UPDATE station                   "
                        "   SET sncf_id = %(sncf_id)s,    "
                        "       nom = %(nom)s,            "
                        "       ville = %(ville)s,        "
                        "       latitude = %(latitude)s,  "
                        "       longitude = %(longitude)s "
                        "WHERE id = %(id)s;               ",
                        {
                            "id": station.id,
                            "sncf_id": station.sncf_id,
                            "nom": station.nom,
                            "ville": station.ville,
                            "latitude": station.latitude,
                            "longitude": station.longitude
                        },
                    )
                    nb_rows = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise
        return nb_rows == 1

    @log
    def delete(self, station) -> bool:
        """Supprime une station de la base de données
        Args:
            station (Station): la station à supprimer
        Returns:
            True si la station a été supprimée, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM station "
                        "WHERE id = %(id)s   ",
                        {"id": station.id},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise
        return res > 0

    @log
    def find_all(self) -> list[Station]:
        """Récupère toutes les gares de la base de données"""
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *              "
                        "FROM station          "
                        "ORDER BY nom;         ",
                        {},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logger.error(e)
            raise
        stations = []
        if res:
            for row in res:
                stations.append(Station(id=row["id"], sncf_id=row["sncf_id"],
                                        nom=row["nom"], ville=row["ville"],
                                        latitude=row["latitude"], longitude=row["longitude"]))
        return stations

    @log
    def find_by_name(self, nom: str) -> list[Station]:
        """Trouve les gares dont le nom contient la saisie (insensible à la casse)"""
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                        "
                        "FROM station                    "
                        "WHERE nom ILIKE %(nom)s         "
                        "ORDER BY nom;                   ",
                        {"nom": f"%{nom}%"}, # %nom% permet de trouver toutes les chaines de caractères qui contiennent nom (Ex: avec "rennes", on pourra avoir "Gare de Rennes", sans les pourcentages, on ne l'aurait pas eu
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logger.error(e)
            raise
        stations = []
        if res:
            for row in res:
                stations.append(Station(id=row["id"], sncf_id=row["sncf_id"],
                                        nom=row["nom"], ville=row["ville"],
                                        latitude=row["latitude"], longitude=row["longitude"]))
        return stations


# Note pour Adam
# Tu peux prendre comme exemple ce fichier pour chaque DAO, dans la structure et le début de chaque méthode/fonction, 
# tout sera similairement la même chose
# Que ce fichier DAO est correct, les autres sont des anciens qui ne prennent pas en compte la base de données 
# (ou ne sont juste pas faits)
# Pour chaque DAO, il faut d'abord que tu changes les business_object correspondant pour qu'ils soient adaptés avec 
# la base de données. Pour voir ce qu'il y a dans chaque objet, tu vas voir ce qu'il y a dans la table correspondante
# dans le fichier data/init_db.sql. Il faut surtout changer les noms pour qu'ils soient adaptés et rajouter ou retirer 
# des paramètres dans le constructeur de chaque classe.abs
# Ensuite, tu peux adapter le DAO en t'inspirant de celui-ci en remplçant les bons paramètres et les bons objets qui
# correspondent à ta classe que tu t'occupes
# Pas besoin de tout faire tout de suite, en faire au moins 2 seraient top pour qu'on puisse déjà commencer des pseudo-tests
