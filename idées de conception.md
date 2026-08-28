### Backend
3 bases de données
# 1ère BDD
BDD des comptes utilisateur
colonnes: nom de compte, mot de passe, email, niveau d'habilitation, abonnement
# 2ème BDD
BDD des gares
colonnes: nom de gare, lieu, nb de voies, type de gare?
# 3ème BDD
BDD des trajets (des trains)
colonnes: gare de départ, date de départ, gare d'arrivée, date d'arrivée, nb de place, nb de place libre, nb de voitures, durée trajet, prix billet
"""possibilité que les trajets soient gare à gare et qu'il y ait une colonne de numéro du train"""
# 4ème BDD
BDD d'adjacence des gares
colonnes: gare 1, gare 2, type de voie
# 5ème BDD
BDD des types d'abonnement
colonnes: réduction, conditions
# 6ème BDD
BDD des tickets
colonnes: utilisateur, trajet