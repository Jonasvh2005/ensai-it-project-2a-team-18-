# Concurrent SNCF

Projet informatique de 2A à l'ENSAI — Groupe 18, année 2026-2027.

**Concurrent SNCF** est une plateforme de vente de trajets ferroviaires conçue pour une société de transport exploitant le réseau SNCF. Le projet s'appuie sur l'API SNCF/Navitia pour récupérer les informations sur les gares et les itinéraires, ainsi que sur une base PostgreSQL pour stocker les données propres à l'application.

> **État du projet :** le dépôt contient actuellement un prototype fonctionnel de l'API de gestion des lignes ainsi qu'une architecture backend en cours de développement. Les fonctionnalités sont donc présentées ci-dessous en distinguant ce qui est actuellement disponible de ce qui est prévu.

## ▶️ Fonctionnalités

Le projet est organisé autour de cinq fonctionnalités principales et de deux fonctionnalités optionnelles.

| Fonctionnalité | Description | État |
|---|---|---|
| **F1 — Gestion des comptes** | Création et connexion des utilisateurs, avec les rôles CLIENT, COLLABORATEUR et ADMIN. | En développement |
| **F2 — Gestion des lignes** | Consultation, création et suppression de lignes d'exploitation entre deux gares. | Prototype disponible |
| **F3 — Gestion des trajets** | Planification, modification et suppression de trajets, avec calcul de la durée via l'API SNCF. | En développement |
| **F4 — Recherche de trajets** | Recherche d'itinéraires entre une gare de départ et une gare d'arrivée. | En développement |
| **F5 — Positionnement commercial** | Proposition de trajets optimaux selon plusieurs critères : durée, prix, correspondances et heure d'arrivée. | À développer |
| **FO1 — Réservation** | Réservation, consultation et annulation d'un trajet. | À développer |
| **FO2 — Classes de voyage** | Choix entre classe standard et classe premium. | À développer |

### Rôles utilisateurs

Trois niveaux d'habilitation sont prévus :

- **CLIENT** : recherche et réservation de trajets ;
- **COLLABORATEUR** : gestion des lignes et de l'offre de trajets ;
- **ADMIN** : gestion des rôles et des habilitations des utilisateurs.

## ▶️ Architecture

Le backend suit une architecture en couches afin de séparer les responsabilités :

```text
Client / Frontend
       │
       ▼
 Controller
       │
       ▼
 Service
       │
       ├──────────────► SNCF Client ──────► API SNCF / Navitia
       │
       ▼
 DAO / Repository
       │
       ▼
 PostgreSQL

 ### Les différentes couches

- **Controller** : expose les endpoints HTTP de l'API.
- **Service** : contient la logique métier.
- **DAO / Repository** : assure l'accès aux données PostgreSQL.
- **Business Object** : représente les principales entités métier.
- **SNCF Client** : centralise les appels à l'API SNCF/Navitia.

Cette organisation permet notamment d'éviter que chaque service réalise directement ses propres appels HTTP vers l'API externe.


## API SNCF / Navitia

Le projet utilise l'API SNCF/Navitia pour récupérer des données qui ne sont pas produites directement par notre application.

Les principaux appels utilisés sont :

| Endpoint Navitia | Utilisation |
|---|---|
| `/places` | Recherche et autocomplétion des gares |
| `/stop_areas` | Récupération des gares pour une éventuelle synchronisation |
| `/lines` | Récupération des lignes commerciales |
| `/journeys` | Recherche d'itinéraires et calcul de la durée des trajets |
| `/stop_areas/{id}/departures` | Récupération des prochains départs d'une gare |

Les appels sont centralisés dans `backend/src/client/sncf_client.py`.

### Authentification à l'API SNCF

Le backend utilise la variable d'environnement :

```text
SNCF_API_TOKEN
```

Exemple :

```bash
export SNCF_API_TOKEN="votre_token"
```

**Ne committez jamais un token API dans le dépôt.** Si un token a déjà été publié dans un fichier ou dans l'historique Git, il doit être révoqué et remplacé.

## Base de données

Le projet utilise **PostgreSQL** pour stocker les données métier.

Le script d'initialisation se trouve dans :

```text
data/init_db.sql
```

Les principales tables sont :

- `users` : comptes utilisateurs et rôles ;
- `station` : gares ;
- `line` : lignes d'exploitation ;
- `line_station` : association entre lignes et gares ;
- `trip` : trajets ;
- `booking` : réservations.

### Variables d'environnement PostgreSQL

La connexion du backend utilise les variables suivantes :

```text
POSTGRES_HOST=
POSTGRES_PORT=5432
POSTGRES_DATABASE=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_SCHEMA=
```

Exemple de fichier `.env` à adapter à votre environnement :

```dotenv
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DATABASE=defaultdb
POSTGRES_USER=user
POSTGRES_PASSWORD=mot_de_passe
POSTGRES_SCHEMA=project

SNCF_API_TOKEN=votre_token
```

Le fichier `.env` est ignoré par Git.

## Structure du projet

```text
.
├── API/
│   ├── base.py
│   ├── main.py
│   ├── sncf.py
│   └── trains.db
│
├── backend/
│   ├── src/
│   │   ├── business_object/
│   │   ├── client/
│   │   ├── controller/
│   │   ├── dao/
│   │   ├── service/
│   │   └── main.py
│   └── tests/
│
├── data/
│   └── init_db.sql
│
├── doc/
│   ├── Diagramme classes.png
│   ├── Diagramme de Gantt.png
│   ├── Diagramme structure projet.png
│   ├── Diagramme séquence.png
│   ├── Diagramme_BDD.png
│   ├── Diagramme_cas_utilisation.png
│   └── tracking/
│
├── docs/
│   ├── api-sncf-notes.md
│   └── code_uml.txt
│
├── opti trajet/
│   ├── algo choix trajet.md
│   └── opti_trajet.py
│
├── rapport/
│   ├── rapport_concurrent_sncf.pdf
│   └── rapport_concurrent_sncf.tex
│
├── structure_bdd.sql
├── Requete_HTTP_API_SNCF.md
├── test.http
├── LICENSE
└── README.md
```

## Prototype actuel

Le dossier `API/` contient un premier prototype permettant de tester les fonctionnalités de gestion des lignes avec FastAPI et une base SQLite locale.

### Lancer le prototype

Depuis le dossier `API/` :

```bash
cd API
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

L'API est alors accessible sur :

```text
http://localhost:5000
```

La documentation interactive FastAPI est disponible à :

```text
http://localhost:5000/docs
```

### Endpoints actuellement disponibles dans le prototype

#### Rechercher une gare

```http
GET /gares?q=Rennes
```

Retourne les gares correspondant à la recherche.

#### Consulter les lignes

```http
GET /lignes
```

#### Créer une ligne

```http
POST /lignes
Content-Type: application/json
```

Exemple :

```json
{
  "depart": "Rennes",
  "arrivee": "Paris"
}
```

#### Supprimer une ligne

```http
DELETE /lignes/{id}
```

## Backend en cours de développement

Le dossier `backend/` correspond à l'architecture cible du projet.

On y retrouve notamment :

```text
backend/src/
├── business_object/
├── client/
├── controller/
├── dao/
└── service/
```

Le client SNCF est déjà structuré dans :

```text
backend/src/client/sncf_client.py
```

Il permet notamment de rechercher des gares, récupérer les gares et lignes SNCF, rechercher des trajets et consulter les départs d'une gare.

La connexion PostgreSQL est centralisée dans :

```text
backend/src/dao/db_connection.py
```

## Tests

Les tests unitaires sont regroupés dans :

```text
backend/tests/
```

Le fichier actuellement présent teste notamment les fonctions de validation des mots de passe et des adresses e-mail.

Pour lancer les tests avec `pytest` :

```bash
pytest
```

> La configuration des dépendances et de l'intégration continue pourra être ajoutée lorsque le fichier de configuration du projet (`pyproject.toml`, workflow GitHub Actions, etc.) sera finalisé.

## Documentation du projet

Les documents de conception sont disponibles dans le dossier `doc/` :

- diagramme de cas d'utilisation ;
- diagramme de classes ;
- diagramme de structure du projet ;
- diagramme de séquence ;
- diagramme de base de données ;
- diagramme de Gantt.

Le rapport complet d'analyse et de conception est disponible dans :

```text
rapport/rapport_concurrent_sncf.pdf
```

Le projet contient également des notes concernant l'API SNCF et l'algorithme de sélection des trajets :

```text
docs/api-sncf-notes.md
opti trajet/algo choix trajet.md
```

## Développement

### Prérequis

- Python 3.10+ recommandé ;
- PostgreSQL pour le backend cible ;
- un compte / token d'accès à l'API SNCF/Navitia ;
- Git.

Les dépendances Python actuellement utilisées par le projet comprennent notamment :

- `fastapi`
- `uvicorn`
- `requests`
- `psycopg2`
- `pydantic`
- `pytest`

Le dépôt ne contient pas encore de fichier de gestion des dépendances (`pyproject.toml` ou `requirements.txt`). Les commandes d'installation devront donc être adaptées à l'environnement de développement retenu.

Exemple :

```bash
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn requests psycopg2-binary pydantic pytest
```

Sous Windows :

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install fastapi uvicorn requests psycopg2-binary pydantic pytest
```

## Équipe

**Groupe 18 — ENSAI, 2A, 2026-2027**

- Maxime Yvano
- Jonas Van Hecke
- Noé Sidobre
- Youssouf Adam Ouattara
- Salma Arraji

**Tuteur :** Kévin Leroy

## Licence

Voir le fichier [`LICENSE`](LICENSE) pour les informations relatives à la licence du projet.
