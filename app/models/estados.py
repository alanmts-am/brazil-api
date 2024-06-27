import json as j
from app.models.response import Response


class Estado:
    def __init__(self, response: Response) -> None:
        self.response = response
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

        return self.response.sucess('estados', estados)

    def get_by_id(self, id: int):
        for e in self.get_all()['estados']:
            if e['id'] == id:
                return self.response.sucess('estado', [e])

    def get_names_only(self):
        estados_nome = []

        for e in self.get_all()['estados']:
            estados_nome.append(e['nome'])

        return self.response.sucess('nomes', sorted(estados_nome))

    def get_municipios(self, municipios: list, id_estado: int):
        return []
