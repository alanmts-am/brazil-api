from app.models.municipio import Municipio
from app.models.estado import Estado
from app.models.regiao import Regiao
from app.utils.read_json import get_json


class MunicipioRepository:
    file_path: str = './app/archives/municipios.json'

    def get_municipios(self) -> list[Municipio]:
        municipios: list[Municipio] = []

        for m in get_json(self.file_path):
            id = m['id']
            nome = m['nome']
            estado_ = m['microrregiao']['mesorregiao']['UF']
            regiao_ = estado_['regiao']

            regiao = Regiao(id=regiao_['id'], sigla=regiao_[
                            'sigla'], nome=regiao_['nome'])
            estado = Estado(id=estado_['id'], sigla=estado_['sigla'],
                            nome=estado_['nome'], regiao=regiao)
            municipio = Municipio(id=id, nome=nome, estado=estado)
            municipios.append(municipio)

        return municipios
