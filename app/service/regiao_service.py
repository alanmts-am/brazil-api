from app.models.regiao import Regiao
from app.models.estado import Estado
from app.models.municipio import Municipio

from app.repository.regiao_repository import RegiaoRepository


class RegiaoService:
    def __init__(self) -> None:
        self.respository = RegiaoRepository()
        pass

    def get_all(self) -> list[Regiao]:
        try:
            return self.respository.get_paises()
        except Exception as e:
            print(e)
            return None

    def get_by_id(self, id: int) -> Regiao:
        try:
            regioes = self.respository.get_paises()

            for regiao in regioes:
                if (regiao.id == id):
                    return regiao
            return []
        except Exception as e:
            print(e)
            return None

    def get_names_only(self) -> list[str]:
        try:
            regioes: list[Regiao] = []

            for regiao in self.respository.get_paises():
                regioes.append(regiao.nome)

            return sorted(regioes)
        except Exception as e:
            print(e)
            return None

    def get_estados(self, estados: list[Estado], id_regiao: int) -> list[Estado]:
        try:
            estados_regiao: list[Estado] = []
            for estado in estados:
                regiao = estado.regiao
                if regiao.id == id_regiao:
                    estados_regiao.append(estado)

            return estados_regiao
        except Exception as e:
            print(e)
            return None

    def get_estado(self, estados: list[Estado], id_regiao: int, id_estado: int) -> Estado:
        try:
            for estado in estados:
                regiao = estado.regiao
                if estado.id == id_estado and regiao.id == id_regiao:
                    return estado
            return []
        except Exception as e:
            print(e)
            return None

    def get_municipios(self, municipios: list[Municipio], id_regiao: int, id_estado: int) -> list[Municipio]:
        try:
            municipios_estado: list[Municipio] = []

            for municipio in municipios:
                estado = municipio.estado
                regiao = estado.regiao
                if estado.id == id_estado and regiao.id == id_regiao:
                    municipios_estado.append(municipio)

            return municipios_estado
        except Exception as e:
            print(e)
            return None

    def get_municipio(self, municipios: list[Municipio], id_regiao: int, id_estado: int, id_municipio: int) -> Municipio:
        try:
            for municipio in municipios:
                estado = municipio.estado
                regiao = estado.regiao
                if municipio.id == id_municipio and estado.id == id_estado and regiao.id == id_regiao:
                    return self.response.sucess([municipio])
            return []
        except Exception as e:
            print(e)
            return None
