from pydantic import BaseModel
from app.models.region import Region


class State(BaseModel):
    id: int
    acronym: str
    name: str
    region: Region
