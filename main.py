from fastapi import FastAPI
from models import Reserva 

app = FastAPI()

db_reservas = []

@app.get("/")
def inicio():
    return {"mensaje": "Bienvenido al sistema de reservas del ITM"}