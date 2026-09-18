from business_object.booking import Booking
from dao.db_connection import DBConnection


class BookingDao:
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
                        "INSERT INTO booking() VALUES" #PAS FINI
                    )