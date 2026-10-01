"""Client technique vers l'API SNCF (Navitia)."""
import os

import requests

BASE_URL = "https://api.sncf.com/v1/coverage/sncf"


class SncfClient:
    def __init__(self, token=None):
        self.token = token or os.environ["SNCF_API_TOKEN"]

    def _get(self, endpoint, params=None):
        response = requests.get(
            f"{BASE_URL}/{endpoint}",
            auth=(self.token, ""),
            params=params,
            timeout=5,
        )
        response.raise_for_status()
        return response.json()

    # --- Gares -----------------------------------------------------------
    def search_places(self, query, count=10):
        """Autocomplétion de gares / lieux. ex. q=Rennes"""
        return self._get("places", {"q": query, "count": count})

    def get_stop_areas(self, count=1000):
        """Liste paginée des gares (pour la synchro en base)."""
        return self._get("stop_areas", {"count": count})

    def get_lines(self, count=500):
        """Liste paginée des lignes commerciales (pour la synchro en base)."""
        return self._get("lines", {"count": count})

    # --- Trajets ---------------------------------------------------------
    def search_journeys(self, from_, to_, datetime=None, count=5):
        """Itinéraires entre deux endroits.
        from_/to_ : id Navitia ('stop_area:SNCF:...') ou 'lon;lat'
        datetime  : 'YYYYMMDDTHHMMSS' (ex. 20261015T080000)
        """
        params = {"from": from_, "to": to_, "count": count}
        if datetime:
            params["datetime"] = datetime
        return self._get("journeys", params)

    def get_departures(self, stop_area_id, count=10):
        """Prochains départs d'une gare (temps réel)."""
        return self._get(f"stop_areas/{stop_area_id}/departures", {"count": count})