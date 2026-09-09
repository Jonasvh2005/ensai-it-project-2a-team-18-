import pytest

from .verif_elements import (email_valide, mdp_valide)


@pytest.mark.parametrize(
    "mdp, resultat_attendu",
    [
        ("123ABb_", "mot de passe trop court"),
        ("*112345AabC-", "charactere * non valide"),
        ("1234ab-_cdefg12", "le mdp doit contenir une majuscule")
        ("A123-456@19469", "le mdp doit contenir une minuscule")
        ("Mot_De_Passe@", "le mdp doit contenir un chiffre")
        ("Mdp1213Q1415m", "le mdp doit contenir un charactère spécial")
        ("Mot_De-Passe[securise]", "mdp valide")
    ],
)
def test_mdp_valide(mdp, resultat_attendu):
    assert mdp_valide(mdp) == resultat_attendu


@pytest.mark.parametrize(
    "element, liste, depart,  resultat_attendu",
    [
        ("NOM@prenom@mail.com", "Un email doit contenir un unique @"),
        ("@mail.com", "Un email ne commence pas par @"),
        ("NOM.prenom@mail", "Un email ne se termine pas par .")
        ("Nom.prenom@mail.", "Pas de . immediatement apres le @")
        ("NOM.prenom@mail.com", "Email valide")
    ],
)
def test_email_valide(email, resultat_attendu):
    assert email_valide(email) == resultat_attendu
