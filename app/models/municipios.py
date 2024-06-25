import json as j
from operator import itemgetter
from app.models.response import Response as res


class Municipio:
    def __init__(self) -> None:
        with open('./app/archives/municipios.json', 'rb') as f:
            self.json = j.load(f)

    def get_all(self):
        municipios = []

        for m in self.json:
            municipio = {}
            municipio['id'] = m['id']
            municipio['nome'] = m['nome']
            municipio['estado'] = m['microrregiao']['mesorregiao']['UF']
            municipios.append(municipio)

        return res.sucess('municipios', municipios)

    def get_by_id(self, id: int):
        for municipio in self.get_all()['municipios']:
            if municipio['id'] == id:
                return res.sucess('municipio', [municipio])
        return res.error('Município não encontrado')

    def get_names_only(self):
        municipios = []

        for m in self.get_all()['municipios']:
            municipios.append(m['nome'])

        return res.sucess('municipios', sorted(municipios))
