from fastapi import FastAPI
from models import Reserva
from typing import List 

app = FastAPI()

db_reservas = []

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido al sistema de reservas del ITM"}

@app.post("/reservas")
def registrar_reserva(nueva_reserva: Reserva):
    db_reservas.append(nueva_reserva)
    return {"mensaje": "Reserva registrada con éxito", "data": nueva_reserva}

@app.get("/reservas", response_model=List[Reserva])
def consultar_reservas():
    return db_reservas
