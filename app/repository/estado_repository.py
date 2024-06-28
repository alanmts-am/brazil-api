from app.models.estado import Estado
from app.models.regiao import Regiao
from app.utils.read_json import get_json


class EstadoRepository:
    file_path: str = './app/archives/estados.json'

    def get_estados(self) -> list[Estado]:
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
