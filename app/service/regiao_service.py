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
        try:
            return self.response.sucess(self.get_data())
        except:
            return self.response.error("Erro ao buscar dados das regiões")

    def get_by_id(self, id: int):
        try:
            regioes = self.get_data()

            for regiao in regioes:
                if (regiao.id == id):
                    return self.response.sucess([regiao])
            return self.response.error("Região não encontrado")
        except:
            return self.response.error("Erro ao buscar dados da região")

    def get_names_only(self):
        try:
            regioes: list[Regiao] = []

            for regiao in self.get_data():
                regioes.append(regiao.nome)

            return self.response.sucess(sorted(regioes))
        except:
            return self.response.error("Erro ao buscar os nomes das regiões")

    def get_estados(self, estados: list[Estado], id_regiao: int):
        try:
            estados_regiao: list[Estado] = []
            for estado in estados:
                regiao = estado.regiao
                if regiao.id == id_regiao:
                    estados_regiao.append(estado)

            return self.response.sucess(estados_regiao)
        except:
            return self.response.error("Erro ao buscar dados dos estados")

    def get_estado(self, estados: list[Estado], id_regiao: int, id_estado: int):
        try:
            for estado in estados:
                regiao = estado.regiao
                if estado.id == id_estado and regiao.id == id_regiao:
                    return self.response.sucess([estado])
        except:
            return self.response.error("Erro ao buscar dados do estado")

    def get_municipios(self, municipios: list[Municipio], id_regiao: int, id_estado: int):
        try:
            municipios_estado: list[Municipio] = []

            for municipio in municipios:
                estado = municipio.estado
                regiao = estado.regiao
                if estado.id == id_estado and regiao.id == id_regiao:
                    municipios_estado.append(municipio)

            return self.response.sucess(municipios_estado)
        except:
            return self.response.error("Erro ao buscar dados dos municípios")

    def get_municipio(self, municipios: list[Municipio], id_regiao: int, id_estado: int, id_municipio: int):
        try:
            for municipio in municipios:
                estado = municipio.estado
                regiao = estado.regiao
                if municipio.id == id_municipio and estado.id == id_estado and regiao.id == id_regiao:
                    return self.response.sucess([municipio])
        except:
            return self.response.error("Erro ao buscar dados do município")
