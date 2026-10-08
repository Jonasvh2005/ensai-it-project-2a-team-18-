-----------------------------------------------------
-- Utilisateurs
-----------------------------------------------------
INSERT INTO users(id_user, nom, mail, password, role) VALUES
(999, 'admin',    'admin@rail.fr',     '0000', 'ADMIN'),
(998, 'bruno',    'bruno@rail.fr',     '1234', 'ADMIN'),
(997, 'claire',   'claire@rail.fr',    'abcd', 'COLLABORATEUR'),
(996, 'david',    'david@rail.fr',     'toto', 'COLLABORATEUR'),
(995, 'emma',     'emma@ensai.fr',     'emma', 'CLIENT'),
(994, 'farid',    'farid@ensai.fr',    '9876', 'CLIENT'),
(993, 'gaelle',   'gaelle@ensai.fr',   'aaaa', 'CLIENT');

-----------------------------------------------------
-- Gares
-----------------------------------------------------
INSERT INTO station(id_station, sncf_id, nom, ville, latitude, longitude) VALUES
(999, 'stop_area:SNCF:87471003', 'Rennes',                  'Rennes',     48.1035, -1.6722),
(998, 'stop_area:SNCF:87391003', 'Paris Montparnasse',      'Paris',      48.8410,  2.3200),
(997, 'stop_area:SNCF:87481002', 'Nantes',                  'Nantes',     47.2172, -1.5420),
(996, 'stop_area:SNCF:87474007', 'Brest',                   'Brest',      48.3880, -4.4793),
(995, 'stop_area:SNCF:87478107', 'Saint-Malo',              'Saint-Malo', 48.6464, -2.0060),
(994, 'stop_area:SNCF:87723197', 'Lyon Part-Dieu',          'Lyon',       45.7606,  4.8597),
(993, 'stop_area:SNCF:87751008', 'Marseille Saint-Charles', 'Marseille',  43.3027,  5.3806),
(992, 'stop_area:SNCF:87581009', 'Bordeaux Saint-Jean',     'Bordeaux',   44.8259, -0.5560),
(991, 'stop_area:SNCF:87286005', 'Lille Flandres',          'Lille',      50.6366,  3.0707),
(990, 'stop_area:SNCF:87686006', 'Paris Gare de Lyon',      'Paris',      48.8443,  2.3744);

-----------------------------------------------------
-- Lignes
-----------------------------------------------------
INSERT INTO line(id_line, sncf_id, code, nom) VALUES
(999, 'line:SNCF:PARIS-BREST',     'PB',  'Paris Montparnasse - Brest'),
(998, 'line:SNCF:RENNES-STMALO',   'RSM', 'Rennes - Saint-Malo'),
(997, 'line:SNCF:NANTES-RENNES',   'NR',  'Nantes - Rennes'),
(996, 'line:SNCF:PARIS-BORDEAUX',  'PBX', 'Paris Montparnasse - Bordeaux'),
(995, 'line:SNCF:PARIS-MARSEILLE', 'PM',  'Paris Gare de Lyon - Marseille'),
(994, 'line:SNCF:LILLE-LYON',      'LL',  'Lille - Lyon');

-----------------------------------------------------
-- Gares de chaque ligne (dans l'ordre)
-----------------------------------------------------
INSERT INTO line_station(id_line, id_station, position) VALUES
(999, 998, 1), (999, 999, 2), (999, 996, 3),
(998, 999, 1), (998, 995, 2),
(997, 997, 1), (997, 999, 2),
(996, 998, 1), (996, 992, 2),
(995, 990, 1), (995, 994, 2), (995, 993, 3);

-----------------------------------------------------
-- Trajets
-----------------------------------------------------
INSERT INTO trip(id_trip, dep_station_id, arr_station_id, dep_datetime, arr_datetime, statut, creator_id) VALUES
(999, 999, 998, '2026-10-01 07:05', '2026-10-01 08:35', 'scheduled', 997),
(998, 999, 998, '2026-10-05 18:05', '2026-10-05 19:35', 'scheduled', 997),
(997, 999, 998, '2026-11-10 07:05', '2026-11-10 08:35', 'scheduled', 997),
(996, 998, 999, '2026-11-12 09:00', '2026-11-12 10:30', 'scheduled', 996),
(995, 999, 996, '2026-11-15 08:10', '2026-11-15 10:15', 'scheduled', 996),
(994, 999, 995, '2026-11-20 12:00', '2026-11-20 12:55', 'scheduled', 997),
(993, 997, 999, '2026-11-22 06:30', '2026-11-22 07:45', 'scheduled', 996),
(992, 998, 992, '2026-12-01 10:00', '2026-12-01 12:05', 'scheduled', 997),
(991, 994, 993, '2026-12-05 14:30', '2026-12-05 16:10', 'cancelled', 997),
(990, 990, 993, '2026-12-20 07:00', null,               'scheduled', null);

-----------------------------------------------------
-- Réservations
-----------------------------------------------------
INSERT INTO booking(id_booking, user_id, trip_id, statut, date_reservation) VALUES
(999, 995, 999, 'confirmed', '2026-09-20 10:00'),
(998, 995, 997, 'confirmed', '2026-10-03 14:30'),
(997, 995, 992, 'cancelled', '2026-10-04 09:15'),
(996, 994, 998, 'confirmed', '2026-09-30 18:45'),
(995, 994, 997, 'confirmed', '2026-10-06 11:00'),
(994, 994, 994, 'confirmed', '2026-10-07 16:20'),
(993, 995, 991, 'cancelled', '2026-10-02 08:00');
