from app.models.regiao import Regiao


class Estado:
    def __init__(self, id, sigla, nome, regiao: Regiao) -> None:
        self.id = id
        self.sigla = sigla
        self.nome = nome
        self.regiao = regiao
        pass
