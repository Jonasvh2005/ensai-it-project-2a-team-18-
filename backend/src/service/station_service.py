from fastapi import HTTPException

from business_object.station import Station
from client.sncf_client import SncfClient
from dao.station_dao import StationDao
from utils.log_utils import log


class StationService:
    """Service qui gère la logique métier liée aux gares
    (création, recherche, synchronisation avec l'API SNCF)."""

    @log
    def create(self, nom, ville, sncf_id=None, latitude=None, longitude=None) -> Station:
        """Crée une nouvelle gare dans le système.
        Args:
            nom (str)
            ville (str)
            sncf_id (str, optional): identifiant Navitia, ex "stop_area:SNCF:87471003"
            latitude (float, optional)
            longitude (float, optional)
        Returns:
            Station créée, ou None si la création a échoué.
        Raises:
            HTTPException: 400 si une gare avec le même sncf_id existe déjà.
        """
        if sncf_id and self.sncf_id_already_used(sncf_id):
            raise HTTPException(
                status_code=400,
                detail="Une gare avec cet identifiant SNCF existe déjà.",
            )

        new_station = Station(
            nom=nom,
            ville=ville,
            sncf_id=sncf_id,
            latitude=latitude,
            longitude=longitude,
        )
        return new_station if StationDao().create(new_station) else None

    @log
    def import_from_sncf(self, query: str) -> list[Station]:
        """Recherche des gares via l'API SNCF et enregistre
        celles qui ne sont pas déjà en base.

        Sert à alimenter la table station.
        Args:
            query (str): saisie utilisateur, ex "Rennes"
        Returns:
            list[Station]: gares correspondantes (déjà connues ou nouvellement importées)
        """
        stations = []
        places = SncfClient().search_places(query).get("places", [])

        for place in places:
            # On ne garde que les gares (stop_area),
            # pas les adresses ou les points d'arrêt (quais).
            if place.get("embedded_type") != "stop_area":
                continue

            coord = place.get("stop_area", {}).get("coord", {})
            regions = place.get("administrative_regions") or []
            station = Station(
                sncf_id=place["id"],
                nom=place.get("name"),
                ville=regions[0].get("name") if regions else None,
                latitude=coord.get("lat"),
                longitude=coord.get("lon"),
            )

            if not self.sncf_id_already_used(station.sncf_id):
                StationDao().create(station)
            stations.append(station)

        return stations

    @log
    def find_all(self) -> list[Station]:
        """Récupère toutes les gares de la base de données.
        Returns:
            list[Station]
        """
        return StationDao().find_all()

    @log
    def find_by_id(self, id_station: int) -> Station:
        """Trouve une gare à partir de son id.
        Args:
            id_station (int)
        Returns:
            Station si trouvée, sinon None.
        """
        return StationDao().find_by_id(id_station)

    @log
    def find_by_name(self, nom: str) -> list[Station]:
        """Trouve les gares dont le nom contient la saisie (insensible à la casse).

        Sert notamment à transformer la saisie d'un utilisateur ("rennes")
        en gare de la base pour la recherche de trajets.
        Args:
            nom (str)
        Returns:
            list[Station]
        """
        return StationDao().find_by_name(nom)

    @log
    def update(self, station) -> Station:
        """Met à jour les informations d'une gare.
        Args:
            station (Station): la gare contenant les informations à jour
        Returns:
            La gare mise à jour, ou None si l'update a échoué.
        """
        return station if StationDao().update(station) else None

    @log
    def delete(self, station) -> bool:
        """Supprime une gare.
        Args:
            station (Station): la gare à supprimer
        Returns:
            True si la suppression a réussi, False sinon.
        """
        return StationDao().delete(station)

    @log
    def sncf_id_already_used(self, sncf_id: str) -> bool:
        """Vérifie si une gare avec cet identifiant SNCF existe déjà.
        Args:
            sncf_id (str)
        Returns:
            True si le sncf_id existe déjà en base.
        """
        stations = StationDao().find_all()
        return sncf_id in [station.sncf_id for station in stations]
