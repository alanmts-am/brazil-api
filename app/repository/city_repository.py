from app.models.city import City
from app.models.state import State
from app.models.region import Region
from app.utils.read_json import get_json


class CityRepository:
    file_path: str = './app/archives/cities.json'

    def get_cities(self) -> list[City]:
        cities: list[City] = []

        for m in get_json(self.file_path):
            id = m['id']
            name = m['nome']
            state_ = m['microrregiao']['mesorregiao']['UF']
            region_ = state_['regiao']

            region = Region(id=region_['id'], acronym=region_[
                            'sigla'], name=region_['nome'])
            state = State(id=state_['id'], acronym=state_['sigla'],
                          name=state_['nome'], region=region)
            municipio = City(id=id, name=name, state=state)
            cities.append(municipio)

        return cities
