import json as j
from operator import itemgetter
from app.models.response import Response as res


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

        return res.sucess('regioes', regioes)

    def get_by_id(self, id: int) -> list:
        regioes = self.get_all()['regioes']

        for regiao in regioes:
            if (regiao['id'] == id):
                return regiao
        return {'error': 'Região não encontrada'}

    def get_names_only(self) -> list:
        regioes = []

        for r in self.get_all()['regioes']:
            regioes.append(r['nome'])

        return res.sucess('regiao', sorted(regioes))

    def get_estados(self, estados: list, id_regiao: int):
        estados_regiao = []
        for estado in estados:
            if estado['regiao']['id'] == id_regiao:
                estados_regiao.append(estado)

        return res.sucess('estados', estados_regiao)

    def get_municipios_from_estado(self, municipios: list, id_regiao: int, id_estado: int):
        municipios_estado = []

        for municipio in municipios:
            if municipio['estado']['id'] == id_estado and municipio['estado']['regiao']['id'] == id_regiao:
                municipios_estado.append(municipio)

        return res.sucess('municipios', municipios_estado)

    def get_estado(self, estados: list, id_regiao: int, id_estado: int):
        for estado in estados:
            if estado['id'] == id_estado and estado['regiao']['id'] == id_regiao:
                return res.sucess('estado', [estado])

    def get_municipio(self, municipios: list, id_regiao: int, id_estado: int, id_municipio: int):
        for municipio in municipios:
            if municipio['id'] == id_municipio and municipio['estado']['id'] == id_estado and municipio['estado']['regiao']['id'] == id_regiao:
                return res.sucess('estado', [municipio])
