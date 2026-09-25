from business_object.booking import Booking
from dao.db_connection import DBConnection
from utils.log_utils import get_logger, log

logger = get_logger(__name__)


class BookingDao:

    @log
    def create(self, booking: Booking) -> bool:
        """ Crée une réservation dans la base de données
        Args:
            booking: La réservation à mettre dans le base de données
        Returns:
            bool: True si la création a bien été faite, False sinon
        """
        res = None

        try:
            with DBConnection.connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO booking(date_reservation, statut) VALUES"
                        "(%(date_reservation)s, %(statut)s)"
                        "RETURNING id;",
                        {
                            "date_reservation": booking.date_reservation,
                            "statut": booking.statut,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        cree = False
        if res:
            booking.id = res["id"]
            cree = True

        return cree

    @log
    def find_by_id(self, id: int) -> Booking:
        """Trouve une réservation à partir de son id
        Args:
            id (int): L'ID de la réservation
        Returns:
            Booking qui correspond à l'id donné
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                       "
                        "FROM booking                   "
                        "WHERE id = %(id)s;             ",
                        {"id": id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logger.error(e)
            raise

        booking = None
        if res:
            booking = Booking(
                id=res["id"],
                date_reservation=res["date_reservation"],
                statut=res["statut"],
            )
        return booking

    @log
    def update(self, booking) -> bool:
        """Update une réservation dans la base de données
        Args:
            booking (Booking): la réservation qui doit être actualisée
        Returns:
            True si actualisée, False sinon
        """
        nb_rows = 0

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE booking                                     "
                        "   SET statut = %(statut)s,                        "
                        "       date_reservation = %(date_reservation)s,    "
                        "WHERE id = %(id)s;                                 ",
                        {
                            "id": booking.id,
                            "date_reservation": booking.date_reservation,
                            "statut": booking.statut,
                        },
                    )
                    nb_rows = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise
        return nb_rows == 1

    @log
    def delete(self, booking) -> bool:
        """Supprime une réservation de la base de données
        Args:
            booking (Booking): la réservation à supprimer
        Returns:
            True si la réservation a été supprimée, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM booking "
                        "WHERE id = %(id)s   ",
                        {"id": booking.id},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logger.error(e)
            raise
        return res > 0
