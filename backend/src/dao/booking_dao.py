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