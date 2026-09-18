class Station:
    """ Classe représentant une gare
    Attributs:
    id: int
    nom: str
    code: str
    """

    def __init__(self, id, nom, code):
        "Constructeur pour la classe Station"
        self.id = id
        self.nom = nom
        self.code = code

    def __str__(self) -> str:
        """Méthode spéciale pour afficher la gare
        Return
        ------
        str: Affichage de la gare
        """
        return f"La gare {self.nom} a pour code {self.code}."