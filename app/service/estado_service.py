from app.models.estado import Estado
from app.models.regiao import Regiao
from app.utils.read_json import get_json


class EstadoService:
    def __init__(self) -> None:
        self.file_path = './app/archives/estados.json'
        pass

    def get_data(self) -> list[Estado]:
        estados = []

        for e in get_json(self.file_path):
            id = e['id']
            sigla = e['sigla']
            nome = e['nome']
            regiao_ = e['regiao']

            regiao = Regiao(id=regiao_['id'], sigla=regiao_[
                            'sigla'], nome=regiao_['nome'])
            estado = Estado(id=id, sigla=sigla, nome=nome, regiao=regiao)

            estados.append(estado)

        return estados

    def get_all(self) -> list[Estado]:
        try:
            return self.get_data()
        except Exception as e:
            print(e)
            return None

    def get_by_id(self, id: int) -> Estado:
        try:
            for regiao in self.get_data():
                if regiao.id == id:
                    return regiao

            return []
        except Exception as e:
            print(e)
            return None

    def get_names_only(self):
        try:
            estados_nome: list[str] = []

            for regiao in self.get_data():
                estados_nome.append(regiao.nome)

            return estados_nome
        except Exception as e:
            print(e)
            return None
