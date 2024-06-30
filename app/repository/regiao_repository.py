from app.models.regiao import Regiao
from app.utils.read_json import get_json


class RegiaoRepository:
    file_path: str = './app/archives/regioes.json'

    def get_paises(self) -> list[Regiao]:
        regioes: list[Regiao] = []

        for r in get_json(self.file_path):
            id = r['id']
            sigla = r['sigla']
            nome = r['nome']
            regiao = Regiao(id=id, sigla=sigla, nome=nome)
            regioes.append(regiao)
        return regioes
