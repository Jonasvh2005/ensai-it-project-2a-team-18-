class Trip:
    """Classe représentant un trajet en train
    Attributs:
    id: int
    date_dep: datetime
    date_arr: datetime
    """

    def __init__(self, id, prix, gare_dep, gare_arr, date_dep, date_arr, corresp=None):
        "Constructeur pour la classe Trip"
        self.id = id
        self.prix = prix
        self.gare_dep = gare_dep
        self.gare_arr = gare_arr
        self.date_dep = date_dep
        self.date_arr = date_arr
        self.corresp = corresp

    def __str__(self) -> str:
        """Méthode spéciale pour afficher le trajet
        Return
        -------
        str: Affichage du trajet
        """
        return f"Le trajet de {self.gare_dep} à {self.gare_arr} coute {self.prix}, il débutera le {self.date_dep} et arrivera le {self.date_arr}."
