from pydantic import BaseModel


class Region(BaseModel):
    id: int
    acronym: str
    name: str
