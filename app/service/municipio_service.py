from app.models.municipio import Municipio
from app.models.estado import Estado
from app.models.regiao import Regiao
from app.models.response import Response
from app.utils.read_json import get_json


class MunicipioService:
    def __init__(self, response: Response) -> None:
        self.response = response
        self.file_path = './app/archives/municipios.json'
        pass

    def get_data(self) -> list[Municipio]:
        municipios: list[Municipio] = []

        for m in get_json(self.file_path):
            id = m['id']
            nome = m['nome']
            estado_ = m['microrregiao']['mesorregiao']['UF']
            regiao_ = estado_['regiao']

            regiao = Regiao(regiao_['id'], regiao_['sigla'], regiao_['nome'])
            estado = Estado(estado_['id'], estado_['sigla'],
                            estado_['nome'], regiao)
            municipio = Municipio(id, nome, estado)
            municipios.append(municipio)

        return municipios

    def get_all(self):
        return self.response.sucess(self.get_data())

    def get_by_id(self, id: int):
        for municipio in self.get_data():
            if municipio.id == id:
                return self.response.sucess([municipio])
        return self.response.error('Município não encontrado')

    def get_names_only(self):
        municipios: list[Municipio] = []

        for municipio in self.get_data():
            municipios.append(municipio.nome)

        return self.response.sucess(sorted(municipios))
