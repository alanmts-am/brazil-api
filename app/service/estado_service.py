from app.models.estado import Estado
from app.models.regiao import Regiao
from app.interface.response_interface import IResponse
from app.utils.read_json import get_json


class EstadoService:
    def __init__(self, response: IResponse) -> None:
        self.response = response
        self.file_path = './app/archives/estados.json'
        pass

    def get_data(self) -> list[Estado]:
        estados = []

        for e in get_json(self.file_path):
            id = e['id']
            sigla = e['sigla']
            nome = e['nome']
            regiao_ = e['regiao']

            regiao = Regiao(regiao_['id'], regiao_['sigla'], regiao_['nome'])
            estado = Estado(id, sigla, nome, regiao)

            estados.append(estado)

        return estados

    def get_all(self):
        try:
            return self.response.sucess(self.get_data())
        except:
            return self.response.error("Erro ao buscar dados dos estados")

    def get_by_id(self, id: int):
        try:
            for regiao in self.get_data():
                if regiao.id == id:
                    return self.response.sucess([regiao])

            return self.response.error("Estado não encontrado")
        except:
            return self.response.error("Erro ao buscar dados do estado")

    def get_names_only(self):
        try:
            estados_nome: list[str] = []

            for regiao in self.get_data():
                estados_nome.append(regiao.nome)

            return self.response.sucess(sorted(estados_nome))
        except:
            return self.response.error("Erro ao buscar os nomes dos estados")
