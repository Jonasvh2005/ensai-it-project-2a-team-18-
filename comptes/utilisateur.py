
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
        #self.__id = max_id + 1
        self.__nom = nom
        self.__mdp = mdp
        self.__email = email
        self.__role = "CLIENT"
        self.__abonnement = None

    def id(self):
        return self.__id

    def nom(self):
        return self.__nom

    def mdp(self):
        return self.__mdp

    def email(self):
        return self.__email

    def role(self):
        return self.__role

    def abonnement(self):
        return self.__abonnement
    
    def changer_nom(self, nom):
        self.__nom = nom
    
    def changer_mdp(self, mdp):
        self.__mdp = mdp

    def changer_email(self, email):
        self.__email = email

    def changer_role(self, role):
        self.__role = role

    def changer_abonnement(self, abonnement):
        self.__abonnement = abonnement

    def __str__(self):
        return f"Le compte {self.__id} nommé {self.__nom} lié au mail {self.email} a comme role {self.__role}"
