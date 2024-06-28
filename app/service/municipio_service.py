from app.models.municipio import Municipio

from app.repository.municipio_repository import MunicipioRepository


class MunicipioService:
    def __init__(self) -> None:
        self.repository = MunicipioRepository()
        pass

    def get_all(self) -> list[Municipio]:
        try:
            return self.repository.get_municipios()
        except Exception as e:
            print(e)
            return None

    def get_by_id(self, id: int) -> Municipio:
        try:
            for municipio in self.repository.get_municipios():
                if municipio.id == id:
                    return municipio
            return []
        except Exception as e:
            print(e)
            return None

    def get_names_only(self) -> list[str]:
        try:
            municipios: list[Municipio] = []

            for municipio in self.repository.get_municipios():
                municipios.append(municipio.nome)

            return sorted(municipios)
        except:
            return None
