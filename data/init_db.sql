DROP TABLE IF EXISTS users        CASCADE;
DROP TABLE IF EXISTS station      CASCADE;
DROP TABLE IF EXISTS line         CASCADE;
DROP TABLE IF EXISTS line_station CASCADE;
DROP TABLE IF EXISTS trip         CASCADE;
DROP TABLE IF EXISTS booking      CASCADE;

-----------------------------------------------------
-- Utilisateurs
-----------------------------------------------------
CREATE TABLE users (
    id_user   SERIAL PRIMARY KEY,
    nom       VARCHAR(30),
    mail      VARCHAR(50) UNIQUE,
    password  VARCHAR(256),          -- hash (bcrypt/argon2), jamais en clair
    role      VARCHAR(30) DEFAULT 'user'
);

-----------------------------------------------------
-- Gares (données synchronisées depuis l'API SNCF)
-----------------------------------------------------
CREATE TABLE station (
    id_station  SERIAL PRIMARY KEY,
    sncf_id     VARCHAR(256) UNIQUE, -- ex. stop_area:SNCF:87471003
    nom         VARCHAR(50),
    ville       VARCHAR(50),
    latitude    DOUBLE PRECISION,
    longitude   DOUBLE PRECISION
);

-----------------------------------------------------
-- Lignes (données synchronisées depuis l'API SNCF)
-----------------------------------------------------
CREATE TABLE line (
    id_line  SERIAL PRIMARY KEY,
    sncf_id  VARCHAR(256) UNIQUE,    -- ex. line:SNCF:PARIS-LYON
    code     VARCHAR(50),
    nom      VARCHAR(50)
);

-----------------------------------------------------
-- Association ligne <-> gare (relation N-N)
-----------------------------------------------------
CREATE TABLE line_station (
    id_line     INTEGER NOT NULL REFERENCES line(id_line),
    id_station  INTEGER NOT NULL REFERENCES station(id_station),
    position    INTEGER,             -- ordre de la gare sur la ligne
    PRIMARY KEY (id_line, id_station)
);

-----------------------------------------------------
-- Trajets (créés par un utilisateur OU issus de l'API)
-----------------------------------------------------
CREATE TABLE trip (
    id_trip         SERIAL PRIMARY KEY,
    dep_station_id  INTEGER REFERENCES station(id_station),
    arr_station_id  INTEGER REFERENCES station(id_station),
    dep_datetime    TIMESTAMP,       -- PostgreSQL : TIMESTAMP, pas DATETIME
    arr_datetime    TIMESTAMP,
    statut          VARCHAR(30),
    creator_id      INTEGER REFERENCES users(id_user)
);

-----------------------------------------------------
-- Réservations (rattachées à un trip : pas de duplication
-- des gares/horaires, et annulation cohérente)
-----------------------------------------------------
CREATE TABLE booking (
    id_booking        SERIAL PRIMARY KEY,
    user_id           INTEGER NOT NULL REFERENCES users(id_user),
    trip_id           INTEGER NOT NULL REFERENCES trip(id_trip),
    statut            VARCHAR(30) DEFAULT 'confirmed',
    date_reservation  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);