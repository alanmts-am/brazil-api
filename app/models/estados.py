import json as j
from operator import itemgetter

class Estados:
    def __init__(self) -> None:
        with open('./app/archives/estados.json', 'rb') as f:
            self.json = j.load(f)
    
    def getAll(self):
        estados = []

        for e in self.json:
            estado = {}
            estado['id'] = e['id']
            estado['sigla'] = e['sigla']
            estado['nome'] = e['nome']
            estado['regiao'] = e['regiao']['nome']

            estados.append(estado)

        return estados
    
    def getEstadoById(self, id:int):
        for e in self.getAll():
            if e['id'] == id:
                return e
            
    def getNamesOnly(self):
        estados = []

        for e in self.getAll():
            estado = {}
            estado['nome'] = e['nome']

            estados.append(estado)

        return sorted(estados, key=itemgetter("nome") )
