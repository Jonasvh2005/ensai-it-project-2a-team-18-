class Utilisateur:
    """
    Classe représentant les comptes utilisateurs (table `users`)
    Attributs:
        id: int: identifiant du compte (id_user)
        nom: str: nom du compte
        mail: str: email associé au compte
        password: str: mot de passe HACHÉ (jamais en clair)
        role: CLIENT, COLLABORATEUR ou ADMIN: niveau d'accès du compte
    """

    def __init__(self, nom, mail, password, role="CLIENT", id=None):
        self.id = id
        self.nom = nom
        self.mail = mail
        self.password = password
        self.role = role

    def __str__(self):
        return f"Le compte {self.id} nommé {self.nom} lié au mail {self.mail} a comme rôle {self.role}"
