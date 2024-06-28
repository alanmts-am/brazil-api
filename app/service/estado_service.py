from app.models.estado import Estado

from app.repository.estado_repository import EstadoRepository


class EstadoService:
    def __init__(self) -> None:
        self.repository = EstadoRepository()
        pass

    def get_all(self) -> list[Estado]:
        try:
            return self.repository.get_estados()
        except Exception as e:
            print(e)
            return None

    def get_by_id(self, id: int) -> Estado:
        try:
            for regiao in self.repository.get_estados():
                if regiao.id == id:
                    return regiao

            return []
        except Exception as e:
            print(e)
            return None

    def get_names_only(self):
        try:
            estados_nome: list[str] = []

            for regiao in self.repository.get_estados():
                estados_nome.append(regiao.nome)

            return estados_nome
        except Exception as e:
            print(e)
            return None
