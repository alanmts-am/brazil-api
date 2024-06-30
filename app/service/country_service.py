from app.models.country import Country
from app.repository.country_repository import CountryRepository


class CountryService:
    def __init__(self) -> None:
        self.respository = CountryRepository()
        pass

    def get_all(self) -> list[Country]:
        try:
            return self.respository.get_countries()
        except Exception as e:
            print(str(e))
            return None

    def get_by_id(self, id: int) -> Country:
        try:
            for country in self.respository.get_countries():
                if country.id == id:
                    return country
            return []
        except Exception as e:
            print(str(e))
            return None

    def get_names_only(self) -> list[str]:
        try:
            names: list[str] = []
            for country in self.respository.get_countries():
                names.append(country.name)

            return names
        except:
            return []
