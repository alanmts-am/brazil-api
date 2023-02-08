import json as j

class Paises:
    def __init__(self) -> None:
        pass

    def getAll(self):
        paises = []
        with open('./app/archives/paises.json', 'rb') as f:
            json = j.load(f)

        for p in json:
            pais = {}
            pais['id'] = p['id']['M49']
            siglas = []
            siglas.append(p['id']['ISO-ALPHA-2'])
            siglas.append(p['id']['ISO-ALPHA-3'])
            pais['siglas'] = siglas
            pais['nome'] = p['nome']
            pais['regiao'] = p['sub-regiao']['regiao']['nome']
            pais['sub-regiao'] = p['sub-regiao']['nome']
            paises.append(pais)
        
        return paises