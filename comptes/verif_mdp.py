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
            maj = True
        elif uni in [45, 95, 35, 46, 36, 64, 44, 40, 41, 91, 93]:
            carac = True
        else:
            return f"charactère {i} non valide"
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
