from .backend.src.business_object.trip.py import Trip


def tri_desc_fus(list_trip):
    """
    Fonction permettant de trier une liste de Trips en fonction de l'horaire de départ.

    Parameters:

    list_trip: list[Trip]
    """
    n = len(list_trip)
    if len(n <= 1):
        return list_trip
    else:
        liste_1 = list_trip[:n//2]
        liste_2 = list_trip[n//2:]
        tri_desc_fus(liste_1)
        tri_desc_fus(liste_2)
        liste_finale = []
        while (liste_1 != [] and liste_2 != []):
            n1 = len(liste_1)
            n2 = len(liste_2)
            dep_1 = liste_1[n1-1].date_dep
            dep_2 = liste_2[n2-1].date_dep
            if dep_1 > dep_2:
                liste_finale.append(liste_2.pop())
            else:
                liste_finale.append(liste_1.pop())
        if liste_1 == []:
            for _ in len(liste_2):
                liste_finale.append(liste_2.pop())
        else:
            for _ in len(liste_1):
                liste_finale.append(liste_1.pop())
        liste_finale = liste_finale[::-1]
        # on inverse la liste
        return liste_finale


def strictement_pire(liste, trajet):
    """
    Fonction permettant de verifier si un trajet est strictement pire qu'une liste de trajets.

    Parameters:
    trajet: Trip: le trajet à vérifier
    liste: list[Trip]
    """
    ans = False
    for trip in liste:
        if (trip.prix <= trajet.prix and trip.date_arr <= trajet.date_arr and trip.corresp <= trajet.corresp):
            ans = True
    return ans


def ajout_opti(liste, trajet):
    """
    Fonction ajoutant un Trip à une liste de Trip et ne gardant que les éléments optimaux.
    liste est déjà composée de trajets optimaux

    Parameters:
    trajet: Trip: le trajet à ajouter dans la liste s'il est optimal
    liste: list[Trip]
    """
    if strictement_pire(liste, trajet):
        return liste
    ans = [trajet]
    for trip in liste:
        if (trip.prix < trajet.prix or trip.date_arr < trajet.date_arr or trip.corresp < trajet.corresp):
            ans.append(trip)
    return ans

# ## indique une ligne que je n'ai pas codé mais qu'il faudra coder


def trajets_opt(gare_ini, gare_finale, heure_depart):
    """
    Fonction donnant la liste des trajets optimaux en passant de la gare initiale à la gare finale

    Parameters:
    gare_ini: str: gare de départ
    gare_finale: str: gare de départ
    heure_depart: timestamp: date de départ voulu par le client
    """
    # ici, on suppose que la durée du trajet = l'heure de depart choisie
    gares_atteintes = [gare_ini]
    d_trajets_opt_gares = {gare_ini: [(0, heure_depart, -1)]}
    # le tuple correspond à (Prix, heure_d'arrivée, nb de correspondance)
    trajets_finaux = []
    list_trips = []
    # ## Dans l'API, récupérer tous les trajets partant de gare_ini entre t = 0 et t = 3h
    tri_desc_fus(list_trips)
    loop = True
    while loop:
        trip = list_trips.pop()
        gare_dep = trip.gare_dep
        gare_arr = trip.gare_arr
        date_arr = trip.date_arr
        date_dep = trip.date_dep
        # on obtient la gare d'arrivé, de départ, la date d'arrivé et de départ
        (prix, corresp) = ([], [])
        for (prix_dep, d_arr, corr_dep) in d_trajets_opt_gares[gare_dep]:
            if d_arr < date_dep and date_dep + 3 > d_arr:
                prix.append(prix_dep + trip.prix)
                corresp.append(corr_dep + 1)
        # on considère les trajets où on a attendu moins de 3h à la gare de départ (contrainte permettant de ne pas avoir de boucle infinie)
        for i in range(len(prix)):
            trajet = Trip(id=None, prix=prix[i], gare_dep=gare_dep, gare_arr=gare_arr, date_dep=date_dep, date_arr=date_arr, corresp=corresp[i])
            # boucle sur tous les trajets possiblement opti
            if not strictement_pire(trajets_finaux, trajet):
                # on abandonne le trajet s'il en existe un strictement mieux auparavant
                if not (gare_arr in d_trajets_opt_gares):
                    # cas où la gare d'arrivée est une nouvelle gare
                    d_trajets_opt_gares[gare_arr] = [trajet]
                    gares_atteintes.append(gare_arr)
                    # ## on ajoute à liste_trip les trains partant de gare_arr pendant les 3h après date_arr avec les valeurs de trip adequat
                else:
                    d_trajets_opt_gares[gare_arr] = ajout_opti(d_trajets_opt_gares[gare_arr], trajet)
                    # ## on ajoute à liste_trip les trains partant de gare_arr pendant les 3h après date_arr avec les valeurs de trip adequat
        if len(list_trips) == 0:
            loop = False
        tri_desc_fus(list_trips)
    # la boucle s'arrète bien car tous les 3 heures, le trajet actuel ajoute au moins un voyage en train
    # et le prix actuel, nb de correspondance et horaire d'arrivée augmentent tous strictement.
    # ainsi, au bout d'un moment, strictement_pire() devient True et len(list_trips) décroit
    return trajets_finaux
