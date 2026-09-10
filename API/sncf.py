import requests

TOKEN = "3752e9c7-19d8-4b1d-a38a-faf10bcfd4c1"
BASE = "https://api.sncf.com/v1/coverage/sncf"


def chercher_gares(mot):
    # Renvoie une liste de couples (nom, identifiant)
    r = requests.get(BASE + "/places",
                     params={"q": mot, "type[]": "stop_area"},
                     auth=(TOKEN, ""))
    places = r.json()["places"]
    return [(p["name"], p["id"]) for p in places]


def temps_trajet(id_depart, id_arrivee, date_heure):
    # Renvoie la duree en secondes, ou None si pas de train
    r = requests.get(BASE + "/journeys",
                     params={"from": id_depart,
                             "to": id_arrivee,
                             "datetime": date_heure.strftime("%Y%m%dT%H%M%S")},
                     auth=(TOKEN, ""))
    trajets = r.json().get("journeys", [])
    if not trajets:
        return None
    return trajets[0]["duration"]