from app.models.country import Country
from app.utils.read_json import get_json


class CountryRepository:
    file_path: str = './app/archives/countries.json'

    def get_countries(self) -> list[Country]:
        countries = []

        for p in get_json(self.file_path):
            id = p['id']['M49']
            acronym = []
            acronym.append(p['id']['ISO-ALPHA-2'])
            acronym.append(p['id']['ISO-ALPHA-3'])
            name = p['nome']
            region = p['sub-regiao']['regiao']['nome']
            sub_region = p['sub-regiao']['nome']
            country = Country(id=id, acronym=acronym, name=name,
                              region=region, sub_region=sub_region)
            countries.append(country)

        return countries
