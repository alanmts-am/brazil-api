import json as j
from app.models.response import Response


class Municipio:
    def __init__(self, response: Response) -> None:
        self.response = response
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

        return self.response.sucess('municipios', municipios)

    def get_by_id(self, id: int):
        for municipio in self.get_all()['municipios']:
            if municipio['id'] == id:
                return self.response.sucess('municipio', [municipio])
        return self.response.error('Município não encontrado')

    def get_names_only(self):
        municipios = []

        for m in self.get_all()['municipios']:
            municipios.append(m['nome'])

        return self.response.sucess('municipios', sorted(municipios))
