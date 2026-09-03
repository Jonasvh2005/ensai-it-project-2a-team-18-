# Notes — API SNCF (Navitia)

Synthèse de la doc officielle (doc.navitia.io) pour préparer le développement
de `SNCFClientService`, en attendant la réception du token personnel.

## Authentification

- HTTP Basic : username = le token, password = vide
- 3 façons équivalentes :
  - Header : `Authorization: <token>`
  - Curl : `-u <token>:`
  - URL directe : `https://<token>@api.navitia.io/v1/...`
- Le token est actif au maximum 5 minutes après sa création.

## Structure d'une requête

`{root_url}/{path}/{endpoint}?{parameters}`

Exemple : `https://api.navitia.io/v1/coverage/sandbox/journeys?from=...&to=...`

## Endpoints utiles pour le projet

### `/places` — autocomplétion des gares (F2, F4)
- Recherche d'objets géographiques par nom (gares, adresses...)
- Paramètre principal : `q=<terme de recherche>`
- Pas de pagination sur cet endpoint

### `/journeys` — calcul de trajet (F2, F3)
- Paramètres principaux : `from`, `to` (coordonnées ou id de gare), `datetime`
- Réponse contient : `duration` (en secondes), `departure_date_time`, `arrival_date_time`, `sections`
- Un des deux paramètres `from`/`to` est obligatoire (sinon calcul d'isochrone)

## Jeu de données de test ("sandbox")

- Un jeu de données fictif existe pour s'entraîner sans token personnel
- Un token de démonstration est fourni dans la doc, mais limité aux données "sandbox" uniquement
- Utile pour tester la structure des requêtes en attendant notre vrai token

## Limites générales

- Pagination automatique : max 200 objets par requête
- Quota gratuit : 5000 requêtes/jour, 150 000/mois

## Prochaines étapes

- [ ] Tester `/places` et `/journeys` sur le jeu "sandbox" dès que possible
- [ ] Une fois le token reçu, valider les mêmes requêtes sur données réelles
- [ ] Documenter le format exact de réponse JSON pour préparer `SNCFClientService`

Source : https://doc.navitia.io/
