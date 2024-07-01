from app.models.region import Region
from app.utils.read_json import get_json


class RegionRepository:
    file_path: str = './app/archives/regions.json'

    def get_regions(self) -> list[Region]:
        regions: list[Region] = []

        for r in get_json(self.file_path):
            id = r['id']
            acronym = r['sigla']
            name = r['nome']
            region = Region(id=id, acronym=acronym, name=name)
            regions.append(region)
        return regions
