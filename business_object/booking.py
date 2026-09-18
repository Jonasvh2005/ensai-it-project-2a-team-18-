class Booking:
    """ Classe représentant une réservation de trajet
    Attributs:
    id: int
    date_reservation: datetime
    statut: str
    """

    def __init__(self, id, date_reservation, statut):
        "Constructeur de la classe Booking"
        self.id = id
        self.date_reservation = date_reservation
        self.statut = statut

    def __str__(self):
        """Méthode spéciale pour afficher une réservation
        Return
        -------
        str: Affichage de la réservation
        """
        return f"La réservation du {self.date_reservation} est {self.statut}."
