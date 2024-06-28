from pydantic import BaseModel
from app.models.regiao import Regiao


class Estado(BaseModel):
    id: int
    sigla: str
    nome: str
    regiao: Regiao
