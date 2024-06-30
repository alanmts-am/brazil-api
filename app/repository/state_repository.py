from app.models.state import State
from app.models.region import Region
from app.utils.read_json import get_json


class StateRepository:
    file_path: str = './app/archives/states.json'

    def get_states(self) -> list[State]:
        states = []

        for e in get_json(self.file_path):
            id = e['id']
            acronym = e['sigla']
            name = e['nome']
            region_ = e['regiao']

            regiao = Region(id=region_['id'], acronym=region_[
                            'sigla'], name=region_['nome'])
            state = State(id=id, acronym=acronym, name=name, region=regiao)

            states.append(state)

        return states
