import json as j


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

        return municipios

    def get_by_id(self, id: int):
        for municipio in self.get_all():
            if municipio['id'] == id:
                return municipio
        return {'error': 'Município não encontrado'}
