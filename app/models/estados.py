import json as j
from operator import itemgetter


class Estado:
    def __init__(self) -> None:
        with open('./app/archives/estados.json', 'rb') as f:
            self.json = j.load(f)

    def get_all(self):
        estados_dict = {}
        estados = []
        estados_dict['status'] = 'OK'

        for e in self.json:
            estado = {}
            estado['id'] = e['id']
            estado['sigla'] = e['sigla']
            estado['nome'] = e['nome']
            estado['regiao'] = e['regiao']

            estados.append(estado)

        estados_dict['estados'] = estados
        return estados_dict

    def get_by_id(self, id: int):
        estado_dict = {}
        estado = []
        estado_dict['status'] = 'OK'

        for e in self.get_all()['estados']:
            if e['id'] == id:
                estado.append(e)

        estado_dict['estado'] = estado
        return estado_dict

    def get_names_only(self):
        estados_nome = []
        estados = {}
        estados['status'] = 'OK'

        for e in self.get_all():
            estados_nome.append(e['nome'])

        estados['nomes'] = sorted(estados_nome)

        return estados

    def get_municipios_from_estado(self, municipios: list, id_estado: int):
        municipios_estado_dict = {}
        municipios_estado = []
        municipios_estado_dict['status'] = 'OK'

        for municipio in municipios:
            if municipio['estado']['id'] == id_estado:
                municipios_estado.append(municipio)
        municipios_estado_dict['municipios'] = municipios_estado

        return municipios_estado_dict
