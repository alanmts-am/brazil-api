from app.models.city import City

from app.repository.city_repository import CityRepository


class CityService:
    def __init__(self) -> None:
        self.repository = CityRepository()
        pass

    def get_all(self, contains: str) -> list[City]:
        try:
            cities = self.repository.get_cities()
            searched_cities: list[City] = []

            if contains != None:
                for city in cities:
                    if contains.lower() in city.name.lower():
                        searched_cities.append(city)
                return searched_cities
            else:
                return cities

        except Exception as e:
            print(e)
            return None

    def get_by_id(self, id: int) -> City:
        try:
            for city in self.repository.get_cities():
                if city.id == id:
                    return city
            return []
        except Exception as e:
            print(e)
            return None

    def get_names_only(self) -> list[str]:
        try:
            cities: list[str] = []

            for city in self.repository.get_cities():
                cities.append(city.name)

            return sorted(cities)
        except:
            return None
