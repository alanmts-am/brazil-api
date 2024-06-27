import json as j
from app.models.response import Response
from app.models.pais import Pais
from app.utils.read_json import get_json


class PaisService:
    def __init__(self, response: Response) -> None:
        self.file_path = './app/archives/paises.json'
        self.response = response
        pass

    def get_data(self) -> list[Pais]:
        paises = []

        for p in get_json(self.file_path):
            id = p['id']['M49']
            siglas = []
            siglas.append(p['id']['ISO-ALPHA-2'])
            siglas.append(p['id']['ISO-ALPHA-3'])
            nome = p['nome']
            regiao = p['sub-regiao']['regiao']['nome']
            sub_regiao = p['sub-regiao']['nome']
            pais = Pais(id, siglas, nome, regiao, sub_regiao)
            paises.append(pais)

        return paises

    def get_all(self):
        return self.response.sucess(self.get_data())

    def get_by_id(self, id: int):
        for pais in self.get_data():
            if pais.id == id:
                return self.response.sucess([pais])

    def get_names_only(self):
        nomes = []
        for pais in self.get_data():
            nomes.append(pais.nome)

        return self.response.sucess(sorted(nomes))
