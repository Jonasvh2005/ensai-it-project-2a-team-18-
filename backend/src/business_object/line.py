class Line:
    """ Classe représentant une ligne de train
    Attributs:
    id: int
    nom: str
    """

    def __init__(self, id, nom):
        "Constructeur pour la classe Line"
        self.id = id
        self.nom = nom

    def __str__(self) -> str:
        """Méthode spéciale pour afficher une ligne
        Return
        -------
        str: Affichage de la ligne
        """
        return f"Cette ligne est la ligne {self.nom}."