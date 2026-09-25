class Trip:
    """Classe représentant un trajet en train
    Attributs:
    id: int
    date: datetime
    heure_dep: datetime
    heure_arr: datetime
    """

    def __init__(self, id, prix, date, gare_dep, gare_arr, heure_dep, heure_arr):
        "Constructeur pour la classe Trip"
        self.id = id
        self.prix = prix
        self.date = date
        self.gare_dep = gare_dep
        self.gare_arr = gare_arr
        self.heure_dep = heure_dep
        self.heure_arr = heure_arr

    def __str__(self) -> str:
        """Méthode spéciale pour afficher le trajet
        Return
        -------
        str: Affichage du trajet
        """
        return f"Le trajet de {self.gare_dep} à {self.gare_arr} coute {self.prix}, débutera le {self.date} à {self.heure_dep} et arrivera à {self.heure_arr}."
