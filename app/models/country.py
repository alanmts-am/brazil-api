from pydantic import BaseModel


class Country(BaseModel):
    id: int
    acronym: list[str]
    name: str
    region: str
    sub_region: str
