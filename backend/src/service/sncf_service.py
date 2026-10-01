from src.client.sncf_client import SncfClient

client = SncfClient()


def parse_journeys(raw):
    """Transforme la réponse /journeys en liste de Trip (objets métier)."""
    trips = []
    for journey in raw.get("journeys", []):
        sections = journey.get("sections", [])
        first, last = sections[0], sections[-1]
        trips.append(
            {
                "sncf_journey_id": journey.get("id"),
                "dep_station": first.get("from", {}).get("name"),
                "arr_station": last.get("to", {}).get("name"),
                "dep_datetime": first.get("departure_date_time"),
                "arr_datetime": last.get("arrival_date_time"),
                "duration": journey.get("durations", {}).get("total"),
                "co2": journey.get("co2_emission", {}).get("value"),
                "sections": [
                    {
                        "mode": s.get("mode"),
                        "line": (s.get("display_informations") or {}).get("name"),
                        "dep": s.get("departure_date_time"),
                        "arr": s.get("arrival_date_time"),
                    }
                    for s in sections
                ],
            }
        )
    return trips


class SncfService:
    @staticmethod
    def search_trips(depart, arrivee, date):
        """depart/arrivee : noms de gares résolus via /places."""
        from_ = client.search_places(depart)["places"][0]["id"]
        to_ = client.search_places(arrivee)["places"][0]["id"]
        raw = client.search_journeys(from_, to_, datetime=date.replace("-", ""))
        return parse_journeys(raw)

    @staticmethod
    def sync_stations():
        """Récupère les gares SNCF pour insertion en base (via le DAO)."""
        return client.get_stop_areas()