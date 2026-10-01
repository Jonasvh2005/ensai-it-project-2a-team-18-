class Station:
    """ Classe représentant une gare
    Attributs:
    id: int
    nom: str
    sncf_id: str
    ville: str
    latitude: str
    longitude: str
    """

    def __init__(self, sncf_id, nom, ville, latitude, longitude, id=None):
        "Constructeur pour la classe Station"
        self.id = id
        self.nom = nom
        self.sncf_id = sncf_id
        self.ville = ville
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self) -> str:
        """Méthode spéciale pour afficher la gare
        Return
        ------
        str: Affichage de la gare
        """
        return f"La gare {self.nom} se trouvant à {self.ville} a pour code SNCF {self.sncf_id}."
