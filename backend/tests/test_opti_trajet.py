import datetime as dt

import pytest

from .opti_trajet import ajout_opti, strictement_pire, trajets_opt, tri_desc_fus
from .station import Station
from .trip import Trip

gare1 = Station(id=1, nom='rennes', code=1)
gare2 = Station(id=2, nom='paris', code=2)
gare3 = Station(id=3, nom='lyon', code=3)
gare4 = Station(id=4, nom='marseille', code=4)

trip1 = Trip(id=1, prix=20, gare_dep=gare1, gare_arr=gare2, date_dep=dt.datetime(2026, 10, 3, 6), date_arr=dt.datetime(2026, 10, 3, 7, 30))
trip2 = Trip(id=1, prix=30, gare_dep=gare2, gare_arr=gare3, date_dep=dt.datetime(2026, 10, 3, 8), date_arr=dt.datetime(2026, 10, 3, 9, 45))
trip3 = Trip(id=1, prix=40, gare_dep=gare1, gare_arr=gare3, date_dep=dt.datetime(2026, 10, 3, 6), date_arr=dt.datetime(2026, 10, 3, 9))
trip4 = Trip(id=1, prix=20, gare_dep=gare3, gare_arr=gare4, date_dep=dt.datetime(2026, 10, 3, 10), date_arr=dt.datetime(2026, 10, 3, 12))
trip5 = Trip(id=1, prix=60, gare_dep=gare1, gare_arr=gare3, date_dep=dt.datetime(2026, 10, 3, 6), date_arr=dt.datetime(2026, 10, 3, 9))
trip12 = Trip(id=1, prix=50, gare_dep=gare1, gare_arr=gare3, date_dep=dt.datetime(2026, 10, 3, 6), date_arr=dt.datetime(2026, 10, 3, 9, 45), corresp=1)


@pytest.mark.parametrize(
    "list_trip, resultat_attendu",
    [
        ([trip2, trip3, trip4], [trip4, trip2, trip3]),
        ([trip5, trip2, trip4], [trip4, trip2, trip5]),
        ([trip5, trip12], [trip5, trip12]),
    ],
)
def test_tri_desc_fus(list_trip, resultat_attendu):
    assert tri_desc_fus(list_trip) == resultat_attendu


@pytest.mark.parametrize(
    "list_trip, trajet, resultat_attendu",
    [
        ([trip3, trip5], trip12, True),
        ([trip5], trip12, False),
        ([trip2], trip3, False),
    ],
)
def test_strictement_pire(list_trip, trajet, resultat_attendu):
    assert strictement_pire(list_trip, trajet) == resultat_attendu


@pytest.mark.parametrize(
    "list_trip, trajet, resultat_attendu",
    [
        ([trip3, trip5], trip12, [trip3, trip5]),
        ([trip12, trip5], trip3, [trip3]),
        ([trip2, trip5, trip12], trip3, [trip3, trip5]),
        ([trip3], trip5, [trip5, trip3]),
    ],
)
def test_ajout_opti(list_trip, trajet, resultat_attendu):
    assert ajout_opti(list_trip, trajet) == resultat_attendu


@pytest.mark.parametrize(
    "gare_ini, gare_finale, heure_depart, resultat_attendu",
    [

    ],
)
def test_trajets_opt(gare_ini, gare_finale, heure_depart, resultat_attendu):
    assert trajets_opt(gare_ini, gare_finale, heure_depart) == resultat_attendu
