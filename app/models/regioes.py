import json as j
from operator import itemgetter


class Regiao:
    def __init__(self) -> None:
        with open('./app/archives/regioes.json', 'rb') as f:
            self.json = j.load(f)

    def get_all(self) -> list:
        regioes = []

        for r in self.json:
            regiao = {}
            regiao['id'] = r['id']
            regiao['sigla'] = r['sigla']
            regiao['nome'] = r['nome']
            regioes.append(regiao)

        return regioes

    def get_by_id(self, id: int) -> list:
        regioes = self.get_all()

        for regiao in regioes:
            if (regiao['id'] == id):
                return regiao
        return {'error': 'Região não encontrada'}

    def get_names_only(self) -> list:
        regioes = []

        for r in self.get_all():
            regiao = {}
            regiao['nome'] = r['nome']
            regioes.append(regiao)

        return sorted(regioes, key=itemgetter("nome"))

    def get_estados(self, estados: list, id_regiao: int):
        estados_regiao = []
        for estado in estados:
            if estado['regiao']['id'] == id_regiao:
                estados_regiao.append(estado)

        return estados_regiao

    def get_estado(self, estados: list, id_regiao: int, id_estado: int):
        estados_regiao = self.get_estados(
            estados, id_regiao)

        for estado in estados_regiao:
            if estado['id'] == id_estado:
                return estado

    def get_municipio(self, municipios: list, id_regiao: int, id_estado: int, id_municipio: int):
        municipios_estado = []

        for municipio in municipios:
            if municipio['id'] == id_municipio and municipio['estado']['id'] == id_estado and municipio['estado']['regiao']['id'] == id_regiao:
                municipios_estado.append(municipio)

        return municipios_estado
