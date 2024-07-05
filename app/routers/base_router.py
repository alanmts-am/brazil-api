from fastapi.routing import APIRouter
from pydantic import BaseModel


class Base(BaseModel):
    message: str
    info: str


base_router = APIRouter()


@base_router.get("/", response_model=Base)
async def root():
    return Base(message="Welcome!", info="Go to /docs in browser to get info about endpoints")
