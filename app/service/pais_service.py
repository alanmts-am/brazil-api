import json as j
from app.models.pais import Pais
from app.utils.read_json import get_json


class PaisService:
    def __init__(self) -> None:
        self.file_path = './app/archives/paises.json'
        pass

    def get_data(self) -> list[Pais]:
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

    def get_all(self) -> dict[Pais]:
        try:
            return self.get_data()
        except Exception as e:
            print(str(e))
            return None

    def get_by_id(self, id: int) -> Pais:
        try:
            for pais in self.get_data():
                if pais.id == id:
                    return pais
            return []
        except Exception as e:
            print(str(e))
            return None

    def get_names_only(self) -> list[str]:
        try:
            nomes: list[str] = []
            for pais in self.get_data():
                nomes.append(pais.nome)

            return nomes
        except:
            return []
