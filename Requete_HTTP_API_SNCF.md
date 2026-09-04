# Liste des endpoints de l'API
## J'ai utilisé l'extension RapidAPI Client pour avoir les réponses HTTP

Requête à écrire : 
GET https://api.navitia.io/v1/coverage/sncf(ici le endpoint)
Authorization: Token

- /places
Permet de rechercher des objets géographiques ou des gares par autocomplétion (paramètre q). C'est l'endpoint idéal pour transformer une saisie utilisateur (ex. "Lille") en coordonnées GPS ou en identifiant structuré.

- /stop_areas
Renvoie la liste des zones d'arrêt (les gares). Utilisé pour parcourir le référentiel complet des gares, récupérer leurs identifiants (stop_area:SNCF:...), leurs codes UIC et leurs coordonnées GPS.

- /stop_points
Renvoie la liste des points d'arrêt physiques précis (quais, voies, entrées) rattachés aux gares.

- /commercial_modes
Liste les modes commerciaux de transport proposés sur le réseau (ex. TGV, TER, Intercités, Eurostar).

- /physical_modes
Liste les modes physiques de déplacement (ex. Train, Bus, Marche).

- /journeys
Le calculateur d'itinéraires. Il prend en entrée des points de départ (from) et d'arrivée (to) sous forme de coordonnées lon;lat ou d'identifiants, ainsi qu'une date/heure (datetime), puis retourne les options de trajet avec les correspondances, durées et étapes.

- /stop_areas/{id}/departures
Affiche le tableau des prochains départs en temps réel et théoriques depuis une gare spécifique.

- /stop_areas/{id}/arrivals
Affiche le tableau des prochaines arrivées en temps réel et théoriques dans une gare spécifique.

- /schedules ou /stop_schedules
Donne les grilles horaires théoriques (fiches horaires) pour une ligne, un arrêt ou une période donnée.

- /lines
Renvoie la liste des lignes ferroviaires du réseau (ex. une ligne TER spécifique).

- /routes
Liste les parcours (sens de circulation / variantes) rattachés aux lignes.

- /networks
Identifie les réseaux de transport englobés (pour la SNCF, le réseau principal).

- /disruptions
Liste l'ensemble des perturbations en cours ou prévues sur le réseau (travaux, retards, grèves, incidents).

- /line_reports
Donne un état du trafic synthétique par ligne (bulletin d'information sur la circulation).

