from pydantic import BaseModel
from app.models.state import State


class City(BaseModel):
    id: int
    name: str
    state: State
