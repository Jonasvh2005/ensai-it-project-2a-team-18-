différents critère de préférence de trajet:
- Prix $
- Durée de trajet
- date d'arrivée
- nb_correspondances

Algo fonction(gare initiale, gare finale):

Créer liste des gares atteintes.
Créer liste finale
Trier les trajets par date de départ (croissant)
BOUCLE sur les trajets:
    Si la gare de départ appartient au gares atteintes (dans les 12h après arrivée à dite gare) 
        Calculer coût total pour arriver à gare et supprimer si innefficace (au niveau de la gare d'arrivé et de liste finale)
        Si la gare d'arivée est la gare finale, ajouter à liste finale (si efficace) (enlever des éléments de liste finale si besoin)
