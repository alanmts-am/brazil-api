import json as j
from app.models.response import Response


class Pais:
    def __init__(self) -> None:
        self.response = Response()
        with open('./app/archives/paises.json', 'rb') as f:
            self.json = j.load(f)

    def get_all(self):
        paises = []

        for p in self.json:
            pais = {}
            pais['id'] = p['id']['M49']
            siglas = []
            siglas.append(p['id']['ISO-ALPHA-2'])
            siglas.append(p['id']['ISO-ALPHA-3'])
            pais['siglas'] = siglas
            pais['nome'] = p['nome']
            pais['regiao'] = p['sub-regiao']['regiao']['nome']
            pais['sub-regiao'] = p['sub-regiao']['nome']
            paises.append(pais)

        return self.response.sucess('paises', paises)

    def get_by_id(self, id: int):
        for p in self.get_all()['paises']:
            if p['id'] == id:
                return self.response.sucess('pais', [p])

    def get_names_only(self):
        nomes = []
        for p in self.get_all()['paises']:
            nomes.append(p['nome'])

        return self.response.sucess('nomes', sorted(nomes))
