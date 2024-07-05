from fastapi import APIRouter, Query
from app.models.state import State
from app.service.state_service import StateService
from typing import List


state_router = APIRouter()
state_service = StateService()


@ state_router.get('/', response_model=List[State])
async def get_states(contains: str = Query(None, min_length=3)):
    return state_service.get_all(contains)


@ state_router.get('/names', response_model=List[str])
async def geta_estados_name_only():
    return state_service.get_names_only()


@ state_router.get('/{id}', response_model=State)
async def get_state_by_id(id: int):
    return state_service.get_by_id(id)
