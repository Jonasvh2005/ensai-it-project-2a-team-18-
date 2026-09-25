DROP TABLE IF EXISTS user CASCADE;
CREATE TABLE user (
    id      SERIAL PRIMARY KEY,
    nom     VARCHAR(30),
    mail    VARCHAR(50),
    password     VARCHAR(256),
    role    VARCHAR(30)
);

DROP TABLE IF EXISTS station CASCADE;
CREATE TABLE station (
    id          SERIAL PRIMARY KEY,
    sncf_id     VARCHAR(256) UNIQUE,
    nom         VARCHAR(50),
    ville       VARCHAR(50),
    latitude    FLOAT,
    longitude   FLOAT
);

DROP TABLE IF EXISTS line CASCADE;
CREATE TABLE line (
    id      SERIAL PRIMARY KEY,
    sncf_id VARCHAR(256) UNIQUE,
    code    VARCHAR(50),
    nom     VARCHAR(50)
);

DROP TABLE IF EXISTS linestation CASCADE;
CREATE TABLE linestation (
    line_id     INTEGER FOREIGN KEY,
    station_id  INTEGER FOREIGN KEY
)

DROP TABLE IF EXISTS trip CASCADE;
CREATE TABLE trip (
    id              SERIAL PRIMARY KEY,
    dep_station_id  INTEGER,
    arr_station_id  INTEGER,
    dep_datetime    DATETIME,
    arr_datetime    DATETIME,
    statut          VARCHAR(30),
    creator_id      INTEGER      
);

DROP TABLE IF EXISTS booking CASCADE;
CREATE TABLE booking (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER FOREIGN KEY,
    dep_station_id  INTEGER FOREIGN KEY,
    arr_station_id  INTEGER FOREIGN KEY,
    dep_datetime    DATETIME,
    arr_datetime    DATETIME,
    statut          VARCHAR(30)
);