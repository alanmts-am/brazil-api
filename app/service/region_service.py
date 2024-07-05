from app.models.region import Region
from app.models.state import State
from app.models.city import City

from app.repository.region_repository import RegionRepository


class RegionService:
    def __init__(self) -> None:
        self.respository = RegionRepository()
        pass

    def get_all(self, contains: str) -> list[Region]:
        try:
            regions = self.respository.get_regions()
            searched_regions: list[Region] = []

            if contains != None:
                for region in regions:
                    if contains.lower() in region.name.lower():
                        searched_regions.append(region)
                return searched_regions
            else:
                return regions

        except Exception as e:
            print(e)
            return None

    def get_by_id(self, id: int) -> Region:
        try:
            regions = self.respository.get_regions()

            for region in regions:
                if (region.id == id):
                    return region
            return []
        except Exception as e:
            print(e)
            return None

    def get_names_only(self) -> list[str]:
        try:
            regions: list[Region] = []

            for region in self.respository.get_regions():
                regions.append(region.name)

            return sorted(regions)
        except Exception as e:
            print(e)
            return None

    def get_states(self, states: list[State], id_region: int) -> list[State]:
        try:
            states_region: list[State] = []
            for state in states:
                region = state.region
                if region.id == id_region:
                    states_region.append(state)

            return states_region
        except Exception as e:
            print(e)
            return None

    def get_state(self, states: list[State], id_region: int, id_state: int) -> State:
        try:
            for state in states:
                region = state.region
                if state.id == id_state and region.id == id_region:
                    return state
            return []
        except Exception as e:
            print(e)
            return None

    def get_cities(self, cities: list[City], id_region: int, id_state: int) -> list[City]:
        try:
            cities_state: list[City] = []

            for city in cities:
                state = city.state
                region = state.region
                if state.id == id_state and region.id == id_region:
                    cities_state.append(city)

            return cities_state
        except Exception as e:
            print(e)
            return None

    def get_city(self, cities: list[City], id_region: int, id_state: int, id_city: int) -> City:
        try:
            for city in cities:
                state = city.state
                region = state.region
                if city.id == id_city and state.id == id_state and region.id == id_region:
                    return self.response.sucess([city])
            return []
        except Exception as e:
            print(e)
            return None
