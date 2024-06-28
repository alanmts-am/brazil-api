from pydantic import BaseModel
from app.models.estado import Estado


class Municipio(BaseModel):
    id: int
    nome: str
    estado: Estado
