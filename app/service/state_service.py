from app.models.state import State

from app.repository.state_repository import StateRepository


class StateService:
    def __init__(self) -> None:
        self.repository = StateRepository()
        pass

    def get_all(self, contains: str) -> list[State]:
        try:
            states = self.repository.get_states()
            searched_states: list[State] = []

            if contains != None:
                for state in states:
                    if contains.lower() in state.name.lower():
                        searched_states.append(state)
                return searched_states
            else:
                return states
        except Exception as e:
            print(e)
            return None

    def get_by_id(self, id: int) -> State:
        try:
            for regiao in self.repository.get_states():
                if regiao.id == id:
                    return regiao

            return []
        except Exception as e:
            print(e)
            return None

    def get_names_only(self):
        try:
            estados_nome: list[str] = []

            for regiao in self.repository.get_states():
                estados_nome.append(regiao.name)

            return estados_nome
        except Exception as e:
            print(e)
            return None
