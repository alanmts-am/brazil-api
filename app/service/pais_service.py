from app.models.pais import Pais
from app.repository.pais_repository import PaisRepository


class PaisService:
    def __init__(self) -> None:
        self.respository = PaisRepository()
        pass

    def get_all(self) -> dict[Pais]:
        try:
            return self.respository.get_paises()
        except Exception as e:
            print(str(e))
            return None

    def get_by_id(self, id: int) -> Pais:
        try:
            for pais in self.respository.get_paises():
                if pais.id == id:
                    return pais
            return []
        except Exception as e:
            print(str(e))
            return None

    def get_names_only(self) -> list[str]:
        try:
            nomes: list[str] = []
            for pais in self.respository.get_paises():
                nomes.append(pais.nome)

            return nomes
        except:
            return []
