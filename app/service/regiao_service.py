from app.models.regiao import Regiao
from app.models.estado import Estado
from app.models.municipio import Municipio
from app.models.response import Response
from app.utils.read_json import get_json


class RegiaoService:
    def __init__(self, response: Response) -> None:
        self.response = response
        self.file_path = './app/archives/regioes.json'
        pass

    def get_data(self) -> list[Regiao]:
        regioes: list[Regiao] = []

        for r in get_json(self.file_path):
            id = r['id']
            sigla = r['sigla']
            nome = r['nome']
            regiao = Regiao(id, sigla, nome)
            regioes.append(regiao)
        return regioes

    def get_all(self):
        return self.response.sucess('regioes', self.get_data())

    def get_by_id(self, id: int):
        regioes = self.get_data()

        for regiao in regioes:
            if (regiao.id == id):
                return regiao
        return self.response.error('Região não encontrada')

    def get_names_only(self):
        regioes: list[Regiao] = []

        for regiao in self.get_data():
            regioes.append(regiao.nome)

        return self.response.sucess('regiao', sorted(regioes))

    def get_estados(self, estados: list[Estado], id_regiao: int):
        estados_regiao: list[Estado] = []
        for estado in estados:
            regiao = estado.regiao
            if regiao.id == id_regiao:
                estados_regiao.append(estado)

        return self.response.sucess('estados', estados_regiao)

    def get_estado(self, estados: list[Estado], id_regiao: int, id_estado: int):
        for estado in estados:
            regiao = estado.regiao
            if estado.id == id_estado and regiao.id == id_regiao:
                return self.response.sucess('estado', [estado])

    def get_municipios(self, municipios: list[Municipio], id_regiao: int, id_estado: int):
        municipios_estado: list[Municipio] = []

        for municipio in municipios:
            estado = municipio.estado
            regiao = estado.regiao
            if estado.id == id_estado and regiao.id == id_regiao:
                municipios_estado.append(municipio)

        return self.response.sucess('municipios', municipios_estado)

    def get_municipio(self, municipios: list[Municipio], id_regiao: int, id_estado: int, id_municipio: int):
        for municipio in municipios:
            estado = municipio.estado
            regiao = estado.regiao
            if municipio.id == id_municipio and estado.id == id_estado and regiao.id == id_regiao:
                return self.response.sucess('estado', [municipio])
