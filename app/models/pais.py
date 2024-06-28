from pydantic import BaseModel


class Pais(BaseModel):
    id: int
    siglas: list[str]
    nome: str
    regiao: str
    sub_regiao: str
