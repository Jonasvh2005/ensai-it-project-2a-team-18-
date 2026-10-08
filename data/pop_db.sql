-----------------------------------------------------
-- Utilisateurs
-----------------------------------------------------
INSERT INTO users(nom, mail, password, role) VALUES
('admin',    'admin@rail.fr',     '0000', 'ADMIN'),
('bruno',    'bruno@rail.fr',     '1234', 'ADMIN'),
('claire',   'claire@rail.fr',    'abcd', 'COLLABORATEUR'),
('david',    'david@rail.fr',     'toto', 'COLLABORATEUR'),
('emma',     'emma@ensai.fr',     'emma', 'CLIENT'),
('farid',    'farid@ensai.fr',    '9876', 'CLIENT'),
('gaelle',   'gaelle@ensai.fr',   'aaaa', 'CLIENT');

-----------------------------------------------------
-- Gares
-----------------------------------------------------
INSERT INTO station(sncf_id, nom, ville, latitude, longitude) VALUES
('stop_area:SNCF:87471003', 'Rennes',                  'Rennes',     48.1035, -1.6722),
('stop_area:SNCF:87391003', 'Paris Montparnasse',      'Paris',      48.8410,  2.3200),
('stop_area:SNCF:87481002', 'Nantes',                  'Nantes',     47.2172, -1.5420),
('stop_area:SNCF:87474007', 'Brest',                   'Brest',      48.3880, -4.4793),
('stop_area:SNCF:87478107', 'Saint-Malo',              'Saint-Malo', 48.6464, -2.0060),
('stop_area:SNCF:87723197', 'Lyon Part-Dieu',          'Lyon',       45.7606,  4.8597),
('stop_area:SNCF:87751008', 'Marseille Saint-Charles', 'Marseille',  43.3027,  5.3806),
('stop_area:SNCF:87581009', 'Bordeaux Saint-Jean',     'Bordeaux',   44.8259, -0.5560),
('stop_area:SNCF:87286005', 'Lille Flandres',          'Lille',      50.6366,  3.0707),
('stop_area:SNCF:87686006', 'Paris Gare de Lyon',      'Paris',      48.8443,  2.3744);

-----------------------------------------------------
-- Lignes
-----------------------------------------------------
INSERT INTO line(sncf_id, code, nom) VALUES
('line:SNCF:PARIS-BREST',     'PB',  'Paris Montparnasse - Brest'),
('line:SNCF:RENNES-STMALO',   'RSM', 'Rennes - Saint-Malo'),
('line:SNCF:NANTES-RENNES',   'NR',  'Nantes - Rennes'),
('line:SNCF:PARIS-BORDEAUX',  'PBX', 'Paris Montparnasse - Bordeaux'),
('line:SNCF:PARIS-MARSEILLE', 'PM',  'Paris Gare de Lyon - Marseille'),
('line:SNCF:LILLE-LYON',      'LL',  'Lille - Lyon');

-----------------------------------------------------
-- Gares de chaque ligne (dans l'ordre)
-----------------------------------------------------
INSERT INTO line_station(id_line, id_station, position) VALUES
(1, 2,  1), (1, 1, 2), (1, 4, 3),
(2, 1,  1), (2, 5, 2),
(3, 3,  1), (3, 1, 2),
(4, 2,  1), (4, 8, 2),
(5, 10, 1), (5, 6, 2), (5, 7, 3);

-----------------------------------------------------
-- Trajets
-----------------------------------------------------
INSERT INTO trip(dep_station_id, arr_station_id, dep_datetime, arr_datetime, statut, creator_id) VALUES
(1,  2, '2026-10-01 07:05', '2026-10-01 08:35', 'scheduled', 3),
(1,  2, '2026-10-05 18:05', '2026-10-05 19:35', 'scheduled', 3),
(1,  2, '2026-11-10 07:05', '2026-11-10 08:35', 'scheduled', 3),
(2,  1, '2026-11-12 09:00', '2026-11-12 10:30', 'scheduled', 4),
(1,  4, '2026-11-15 08:10', '2026-11-15 10:15', 'scheduled', 4),
(1,  5, '2026-11-20 12:00', '2026-11-20 12:55', 'scheduled', 3),
(3,  1, '2026-11-22 06:30', '2026-11-22 07:45', 'scheduled', 4),
(2,  8, '2026-12-01 10:00', '2026-12-01 12:05', 'scheduled', 3),
(6,  7, '2026-12-05 14:30', '2026-12-05 16:10', 'cancelled', 3),
(10, 7, '2026-12-20 07:00', null,               'scheduled', null);

-----------------------------------------------------
-- Réservations
-----------------------------------------------------
INSERT INTO booking(user_id, trip_id, statut, date_reservation) VALUES
(5, 1, 'confirmed', '2026-09-20 10:00'),
(5, 3, 'confirmed', '2026-10-03 14:30'),
(5, 8, 'cancelled', '2026-10-04 09:15'),
(6, 2, 'confirmed', '2026-09-30 18:45'),
(6, 3, 'confirmed', '2026-10-06 11:00'),
(6, 6, 'confirmed', '2026-10-07 16:20'),
(5, 9, 'cancelled', '2026-10-02 08:00');
