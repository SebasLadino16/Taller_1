from pydantic import BaseModel

class Reserva(BaseModel):
    id_reserva: int
    id_sala: str
    id_usuario: str
    fecha: str
    hora_inicio: str
    hora_fin: str
    personas: int
    estado: str