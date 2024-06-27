from app.models.estado import Estado


class Municipio:
    def __init__(self, id, nome, estado: Estado) -> None:
        self.id = id
        self.nome = nome
        self.estado = estado
        pass
