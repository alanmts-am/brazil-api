from app.models.pais import Pais
from app.utils.read_json import get_json


class PaisRepository:
    file_path: str = './app/archives/paises.json'

    def get_paises(self) -> list[Pais]:
        paises = []

        for p in get_json(self.file_path):
            id = p['id']['M49']
            siglas = []
            siglas.append(p['id']['ISO-ALPHA-2'])
            siglas.append(p['id']['ISO-ALPHA-3'])
            nome = p['nome']
            regiao = p['sub-regiao']['regiao']['nome']
            sub_regiao = p['sub-regiao']['nome']
            pais = Pais(id=id, siglas=siglas, nome=nome,
                        regiao=regiao, sub_regiao=sub_regiao)
            paises.append(pais)

        return paises
