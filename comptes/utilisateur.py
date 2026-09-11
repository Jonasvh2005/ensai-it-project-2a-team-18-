class Utilisateur:
    """
    classe représentant les comptes utilisateurs
    Attributs:
        id: int: identifiant du compte
        nom: str: nom du compte
        mdp: str: mot de passe du compte
        email: str: email associé au compte
        role: CLIENT, COLLABORATEUR ou ADMIN: niveau d'accès du compte
        abbonement: str: abonnement pris (ou None si pas d'abonnement)
    """

    def __init__(self, id, nom, mdp, email):
        self.__id = None
        # self.__id = max_id + 1
        self.nom = nom
        self.mdp = mdp
        self.email = email
        self.role = "CLIENT"
        self.abonnement = None

    def id(self):
        """Fonction permettant de renvoyer l'identifiant de l'utilisateur"""
        return self.__id

    def __str__(self):
        return f"Le compte {self.__id} nommé {self.__nom} lié au mail {self.email} a comme rôle {self.__role}"
