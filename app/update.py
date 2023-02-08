from models.database import Database

db = Database()

db.update('https://servicodados.ibge.gov.br/api/v1/localidades/paises', './app/archives/paises.json')
db.update('https://servicodados.ibge.gov.br/api/v1/localidades/regioes', './app/archives/regioes.json')
db.update('https://servicodados.ibge.gov.br/api/v1/localidades/estados', './app/archives/estados.json')
db.update('https://servicodados.ibge.gov.br/api/v1/localidades/municipios', './app/archives/municipios.json')