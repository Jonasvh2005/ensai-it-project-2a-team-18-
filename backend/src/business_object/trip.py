class Trip:
    """Classe représentant un trajet en train (table `trip`)
    Attributs:
    id: int (id_trip)
    dep_station_id: int: id de la gare de départ
    arr_station_id: int: id de la gare d'arrivée
    dep_datetime: datetime
    arr_datetime: datetime
    statut: str
    creator_id: int: id de l'utilisateur qui a créé le trajet
    """

    def __init__(self, dep_station_id, arr_station_id, dep_datetime, arr_datetime,
                 statut=None, creator_id=None, id=None):
        "Constructeur pour la classe Trip"
        self.id = id
        self.dep_station_id = dep_station_id
        self.arr_station_id = arr_station_id
        self.dep_datetime = dep_datetime
        self.arr_datetime = arr_datetime
        self.statut = statut
        self.creator_id = creator_id

    def __str__(self) -> str:
        """Méthode spéciale pour afficher le trajet
        Return
        -------
        str: Affichage du trajet
        """
        return (f"Le trajet de la gare {self.dep_station_id} à la gare {self.arr_station_id} "
                f"débute le {self.dep_datetime} et arrive le {self.arr_datetime}.")
