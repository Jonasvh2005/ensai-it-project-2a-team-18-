from business_object.utilisateur import Utilisateur
from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log

logger = get_logger(__name__)


class UtilisateurDao:

    @staticmethod
    def _from_row(row) -> Utilisateur:
        return Utilisateur(
            id=row["id_user"],
            nom=row["nom"],
            mail=row["mail"],
            password=row["password"],
            role=row["role"],
        )

    @log
    def create(self, utilisateur: Utilisateur) -> bool:
        """Crée un utilisateur dans la base de données
        Args:
            utilisateur: L'utilisateur à mettre dans la base de données
                (son mot de passe doit déjà être haché)
        Returns:
            bool: True si la création a bien été faite, False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO users(nom, mail, password, role) VALUES "
                        "(%(nom)s, %(mail)s, %(password)s, %(role)s) "
                        "RETURNING id_user;",
                        {
                            "nom": utilisateur.nom,
                            "mail": utilisateur.mail,
                            "password": utilisateur.password,
                            "role": utilisateur.role,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        cree = False
        if res:
            utilisateur.id = res["id_user"]
            cree = True

        return cree

    @log
    def find_by_id(self, id: int) -> Utilisateur:
        """Trouve un utilisateur à partir de son id
        Args:
            id (int): L'ID de l'utilisateur
        Returns:
            Utilisateur qui correspond à l'id donné (None si introuvable)
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM users WHERE id_user = %(id)s;",
                        {"id": id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        return self._from_row(res) if res else None

    @log
    def find_by_mail(self, mail: str) -> Utilisateur:
        """Trouve un utilisateur à partir de son email (utile pour la connexion)
        Args:
            mail (str): L'email de l'utilisateur
        Returns:
            Utilisateur qui correspond au mail donné (None si introuvable)
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM users WHERE mail = %(mail)s;",
                        {"mail": mail},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        return self._from_row(res) if res else None

    @log
    def update(self, utilisateur: Utilisateur) -> bool:
        """Met à jour un utilisateur dans la base de données
        Args:
            utilisateur (Utilisateur): l'utilisateur qui doit être actualisé
        Returns:
            True si actualisé, False sinon
        """
        nb_rows = 0

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE users "
                        "   SET nom = %(nom)s, "
                        "       mail = %(mail)s, "
                        "       password = %(password)s, "
                        "       role = %(role)s "
                        "WHERE id_user = %(id)s;",
                        {
                            "id": utilisateur.id,
                            "nom": utilisateur.nom,
                            "mail": utilisateur.mail,
                            "password": utilisateur.password,
                            "role": utilisateur.role,
                        },
                    )
                    nb_rows = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise
        return nb_rows == 1

    @log
    def delete(self, utilisateur: Utilisateur) -> bool:
        """Supprime un utilisateur de la base de données
        Args:
            utilisateur (Utilisateur): l'utilisateur à supprimer
        Returns:
            True si l'utilisateur a été supprimé, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM users WHERE id_user = %(id)s;",
                        {"id": utilisateur.id},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise
        return res > 0
