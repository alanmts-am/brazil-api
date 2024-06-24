import json as j
from operator import itemgetter


class Estados:
    def __init__(self) -> None:
        with open('./app/archives/estados.json', 'rb') as f:
            self.json = j.load(f)

    def get_all(self):
        estados = []

        for e in self.json:
            estado = {}
            estado['id'] = e['id']
            estado['sigla'] = e['sigla']
            estado['nome'] = e['nome']
            estado['regiao'] = e['regiao']

            estados.append(estado)

        return estados

    def get_by_id(self, id: int):
        for e in self.get_all():
            if e['id'] == id:
                return e

    def get_names_only(self):
        estados = []

        for e in self.get_all():
            estado = {}
            estado['nome'] = e['nome']

            estados.append(estado)

        return sorted(estados, key=itemgetter("nome"))

    def get_municipios_from_estado(self, municipios: list, id_estado: int):
        municipios_estado = []

        for municipio in municipios:
            if municipio['estado']['id'] == id_estado:
                municipios_estado.append(municipio)

        return municipios_estado
