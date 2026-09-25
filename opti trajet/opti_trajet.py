from backend.src.business_object.trip import Trip


def inverse(liste):
    ans = []
    for i in len(liste):
        ans.append(liste.pop)
    return (liste)


def tri_desc_fus(list_trip):
    # trajet(gare_dep, gare_arr, date_dep, date_arr, prix, type)
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
            dep_1 = (liste_1[n1-1].dep, liste_1[n1-1].heure_dep)
            dep_2 = (liste_2[n2-1].dep, liste_2[n2-1].heure_dep)
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
        liste_finale = inverse(liste_finale)
        return liste_finale


def strictement_pire(liste, prix, horaire_arr, corresp):
    ans = False
    for trip in liste:
        if (trip.prix <= prix and trip.horaire_arr <= horaire_arr and trip.corresp <= corresp):
            ans = True
    return ans


def ajout_opti(liste, trip):
    ans = [trip]
    for trajet in liste:
        if (trip.prix > trajet.prix or trip.horaire_arr > trajet.horaire_arr or trip.corresp > trajet.corresp):
            ans.append(trajet)
    return ans

# ## indique une ligne que je n'ai pas codé mais qu'il faudra coder


def trajets_opt(gare_ini, gare_finale, horaire_depart):
    """ici, on suppose que la durée = l'heure de depart choisie"""
    gares_atteintes = voisins(gare_ini)
    # voisins est une liste obtenue par: SELECT gares FROM tableau_adjacence WHERE autre_gare = gare_ini
    d_trajets_opt_gares = {gare_ini: [(0, horaire_depart, -1)]}
    # le tuple correspond à (Prix, horaire_d'arrivée, nb de correspondance)
    trajets_finaux = []
    list_trips = []
    # ## Dans l'API, récupérer tous les trajets partant de gare_ini entre t = 0 et t = 3h
    tri_desc_fus(list_trips)
    loop = True
    while loop:
        trip = list_trips.pop()
        gare_arr = trip.gare_arr
        horaire_arr = (trip.date, trip.heure_arr)
        (prix, corresp) = ([], [])
        for (prix_dep, (date_arr, h_arr), corr_dep) in d_trajets_opt_gares[trip.gare_dep]:
            if h_arr < trip.heure_dep and trip.heure_dep + 3 > h_arr:
                prix.append(prix_dep + trip.prix)
                corresp.append(corr_dep + 1)
        # on obtient la gare de départ, d'arrivée, l'horaire d'arrivée du train et
        # les différents trajets optimaux en revenant au tout début du trajet et leurs prix/corresp
        for i in range(len(prix)):
            # boucle sur tous les trajets possiblement opti
            if not strictement_pire(trajets_finaux, prix[i], horaire_arr, corresp[i]):
                # on abandonne le trajet s'il en existe un strictement mieux auparavant
                if not (gare_arr in d_trajets_opt_gares):
                    # cas où la gare d'arrivée est une nouvelle gare
                    d_trajets_opt_gares[gare_arr] = [(prix[i], horaire_arr, corresp[i])]
                    gares_atteintes.append(gare_arr)
                    # ## on ajoute à liste_trip les trains partant de gare_arr pendant les 3h après horaire_arr avec les valeurs de trip adequat
                else:
                    d_trajets_opt_gares[gare_arr] = ajout_opti(d_trajets_opt_gares[gare_arr], trip)
                    # ## on ajoute à liste_trip les trains partant de gare_arr pendant les 3h après horaire_arr avec les valeurs de trip adequat
        if len(list_trips) == 0:
            loop = False
            tri_desc_fus(list_trips)
    # la boucle s'arrète bien car tous les 3 heures, le trajet actuel ajoute au moins un voyage en train
    # et le prix actuel, nb de correspondance et horaire d'arrivée augmentent tous strictement.
    # ainsi, au bout d'un moment, strictement_pire() devient True et len(list_trips) décroit
    return trajets_finaux
