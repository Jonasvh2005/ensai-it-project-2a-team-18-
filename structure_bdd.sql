-- 1. Table des Types d'Abonnement
CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL, -- ex: 'Carte Jeune', 'Abonnement Pro'
    discount_rate NUMERIC(3,2) NOT NULL DEFAULT 0.00, -- ex: 0.30 pour -30%
    conditions TEXT
);

-- 2. Table des Profils Utilisateurs & Rôles
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('CLIENT', 'COLLABORATEUR', 'ADMIN')),
    subscription_id INT REFERENCES subscriptions(id) -- Optionnel
);

-- 3. Table des Gares Référencées
CREATE TABLE stations (
    id SERIAL PRIMARY KEY,
    sncf_uic_code VARCHAR(50) UNIQUE NOT NULL, -- ID Réseau API SNCF
    name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL
);

-- 4. Table d'Adjacence des Gares & Rails
CREATE TABLE station_adjacencies (
    id SERIAL PRIMARY KEY,
    station_a_id INT REFERENCES stations(id),
    station_b_id INT REFERENCES stations(id),
    rail_type VARCHAR(50) NOT NULL, -- ex: 'LGV', 'Ligne TER'
    distance_km NUMERIC(6,2) NOT NULL
);

-- 5. Table des Trains
CREATE TABLE trains (
    id SERIAL PRIMARY KEY,
    train_number VARCHAR(20) UNIQUE NOT NULL,
    capacity_classique INT NOT NULL DEFAULT 200,
    capacity_premium INT NOT NULL DEFAULT 50
);

-- 6. Table des Trajets Planifiés
CREATE TABLE trips (
    id SERIAL PRIMARY KEY,
    train_id INT REFERENCES trains(id),
    departure_station_id INT REFERENCES stations(id),
    arrival_station_id INT REFERENCES stations(id),
    departure_time TIMESTAMP NOT NULL,
    arrival_time TIMESTAMP NOT NULL,
    duration_minutes INT NOT NULL, -- Calculé via API SNCF
    base_price NUMERIC(8,2) NOT NULL,
    seats_left INT NOT NULL
);

-- 7. Table des Tickets / Réservations
CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    ticket_reference VARCHAR(12) UNIQUE NOT NULL,
    user_id INT REFERENCES users(id),
    trip_id INT REFERENCES trips(id),
    travel_class VARCHAR(20) CHECK (travel_class IN ('CLASSIQUE', 'PREMIUM')),
    final_price NUMERIC(8,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'CONFIRME' CHECK (status IN ('CONFIRME', 'ANNULE'))
);