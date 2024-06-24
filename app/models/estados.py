import json as j
from app.models.response import Response as res


class Estado:
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

        return res.sucess('estados', estados)

    def get_by_id(self, id: int):
        estado = []

        for e in self.get_all()['estados']:
            if e['id'] == id:
                estado.append(e)

        return res.sucess('estado', estado)

    def get_names_only(self):
        estados_nome = []

        for e in self.get_all()['estados']:
            estados_nome.append(e['nome'])

        return res.sucess('nomes', sorted(estados_nome))

    def get_municipios_from_estado(self, municipios: list, id_estado: int):
        municipios_estado = []

        for municipio in municipios:
            if municipio['estado']['id'] == id_estado:
                municipios_estado.append(municipio)

        return res.sucess('municipios', municipios_estado)
