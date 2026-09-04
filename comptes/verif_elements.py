def mdp_valide(mdp) -> str:
    """
    fonction qui vérifie que le mot de passe soit valide.
    Un mot de passe valide contient:
    -10 caractères
    -une majuscule
    -une minuscule
    -un chiffre
    -un caractère spécial ("-", "_", "#", ".", "$", "@", ",", "(", ")", "[", "]")
    """
    if len(mdp) < 10:
        return "mot de passe trop court"
    (maj, min, chiffre, carac) = (False, False, False, False)
    for i in mdp:
        uni = ord(i)
        if uni >= 48 and uni <= 57:
            chiffre = True
        elif uni >= 65 and uni <= 90:
            maj = True
        elif uni >= 97 and uni <= 122:
            min = True
        elif i in ["-", "_", "#", ".", "$", "@", ",", "(", ")", "[", "]"]:
            carac = True
        else:
            return f"charactere '{i}' non valide"
    if not maj:
        return "le mdp doit contenir une majuscule"
    elif not min:
        return "le mdp doit contenir une minuscule"
    elif not chiffre:
        return "le mdp doit contenir un chiffre"
    elif not carac:
        return "le mdp doit contenir un charactère spécial"
    else:
        return "mdp valide"


def email_valide(email) -> str:
    """
    fonction qui vérifie que le mot de passe soit valide.
    Un email valide est de la forme: XXXX@XXXX.XXXX
    -Une chaine de charactères avant un @
    -Une chaine de charactères (pouvant contenir '.') entre le dernier '.' et le '@'
    -Une chaine de charactères
    """
    arobase_split = email.split("@")

    if len(arobase_split) != 2:
        return "Un email doit contenir un unique @"

    if email[0] == "@":
        return "Un email ne commence pas par @"

    if email[-1] == ".":
        return "Un email ne se termine pas par ."

    if len(arobase_split[1][0]) == ".":
        return "Pas de . immediatement apres le @"

    return "Email valide"
