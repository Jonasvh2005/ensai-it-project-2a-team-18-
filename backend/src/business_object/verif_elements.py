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
    (maj, minu, chiffre, carac) = (False, False, False, False)
    for i in mdp:
        uni = ord(i)
        if uni >= 48 and uni <= 57:
            # cela corespond aux chiffres arabes
            chiffre = True
        elif uni >= 65 and uni <= 90:
            # cela corespond aux lettres majuscules de l'alphabet latin moderne
            maj = True
        elif uni >= 97 and uni <= 122:
            # cela corespond aux lettres minuscules de l'alphabet latin moderne
            minu = True
        elif i in ["-", "_", "#", ".", "$", "@", ",", "(", ")", "[", "]"]:
            # cela correspnd à une sélection de charactères spéciaux
            carac = True
        else:
            return f"charactere '{i}' non valide"
    if not maj:
        return "le mdp doit contenir une majuscule"
    elif not minu:
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
    -Une chaine de charactères avant un unique @
    -Une chaine de charactères entre le '@' et le '.'
    -Une chaine de charactères après le dernier '.'
    """
    arobase_split = email.split("@")
    particule = arobase_split[1].split(".")

    if len(arobase_split) != 2:
        return "Un email doit contenir un unique '@'"

    if email[0] == "@":
        return "Un email ne commence pas par '@'"

    if len(particule) < 2:
        return "Un email doit contenir un point apres le '@'"

    if email[-1] == ".":
        return "Un email ne se termine pas par '.'"

    if arobase_split[1][0] == ".":
        return "Pas de '.' immediatement apres le '@'"

    return "Email valide"
