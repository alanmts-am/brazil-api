from pydantic import BaseModel


class Regiao(BaseModel):
    id: int
    sigla: str
    nome: str
