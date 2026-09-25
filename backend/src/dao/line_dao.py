from business_object.line import Line
from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log

logger = get_logger(__name__)


class LineDao:

    @log
    def create(self, line: Line) -> bool:
        """ Crée une ligne dans la base de données
        Args:
            line: La ligne à mettre dans le base de données
        Returns:
            bool: True si la création a bien été faite, False sinon
        """
        res = None

        try:
            with DBConnection.connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO line(nom) VALUES"
                        "(%(nom)s"
                        "RETURNING id;",
                        {
                            "nom": line.nom,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        cree = False
        if res:
            line.id = res["id"]
            cree = True

        return cree

    @log
    def find_by_id(self, id: int) -> Line:
        """Trouve une ligne à partir de son id
        Args:
            id (int): L'ID de la ligne
        Returns:
            Line qui correspond à l'id donné
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                       "
                        "FROM line                   "
                        "WHERE id = %(id)s;             ",
                        {"id": id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        line = None
        if res:
            line = Line(
                id=res["id"],
                nom=res["nom"],
            )
        return line

    @log
    def update(self, line) -> bool:
        """Update une ligne dans la base de données
        Args:
            line (Line): la ligne qui doit être actualisée
        Returns:
            True si actualisée, False sinon
        """
        nb_rows = 0

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE line             "
                        "   SET nom = %(nom)s,   "
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
