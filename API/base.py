import sqlite3


def connexion():
    conn = sqlite3.connect("trains.db")
    conn.row_factory = sqlite3.Row
    return conn


def creer_tables():
    conn = connexion()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS lignes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            depart_nom TEXT,
            depart_id TEXT,
            arrivee_nom TEXT,
            arrivee_id TEXT
        )
    """)
    conn.commit()
    conn.close()


def ajouter_ligne(depart_nom, depart_id, arrivee_nom, arrivee_id):
    conn = connexion()
    cur = conn.execute(
        "INSERT INTO lignes (depart_nom, depart_id, arrivee_nom, arrivee_id) VALUES (?, ?, ?, ?)",
        (depart_nom, depart_id, arrivee_nom, arrivee_id))
    conn.commit()
    numero = cur.lastrowid
    conn.close()
    return numero


def lister_lignes():
    conn = connexion()
    resultats = conn.execute("SELECT * FROM lignes").fetchall()
    conn.close()
    return [dict(r) for r in resultats]


def supprimer_ligne(numero):
    conn = connexion()
    cur = conn.execute("DELETE FROM lignes WHERE id = ?", (numero,))
    conn.commit()
    conn.close()
    return cur.rowcount > 0
