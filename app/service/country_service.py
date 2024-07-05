from app.models.country import Country
from app.repository.country_repository import CountryRepository


class CountryService:
    def __init__(self) -> None:
        self.respository = CountryRepository()
        pass

    def get_all(self, search: str) -> list[Country]:
        try:
            countries = self.respository.get_countries()
            searched_countries: list[Country] = []

            if search != None:
                for country in countries:
                    if search.lower() in country.name.lower():
                        searched_countries.append(country)

                return searched_countries
            else:
                return countries

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
