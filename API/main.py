import base
import sncf
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API Trains", root_path="/proxy/5000")
base.creer_tables()


class NouvelleLigne(BaseModel):
    depart: str
    arrivee: str


@app.get("/gares")
def rechercher_gares(q: str):
    return [{"nom": n, "id": i} for n, i in sncf.chercher_gares(q)]


@app.get("/lignes")
def voir_lignes():
    return base.lister_lignes()


@app.post("/lignes")
def creer_ligne(ligne: NouvelleLigne):
    depart = sncf.chercher_gares(ligne.depart)
    arrivee = sncf.chercher_gares(ligne.arrivee)

    if not depart or not arrivee:
        raise HTTPException(404, "Gare introuvable")

    numero = base.ajouter_ligne(depart[0][0], depart[0][1],
                                arrivee[0][0], arrivee[0][1])
    return {"id": numero, "depart": depart[0][0], "arrivee": arrivee[0][0]}


@app.delete("/lignes/{numero}")
def effacer_ligne(numero: int):
    if not base.supprimer_ligne(numero):
        raise HTTPException(404, "Ligne introuvable")
    return {"message": "Ligne supprimee"}
