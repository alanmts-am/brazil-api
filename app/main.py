from app.routers.paises import paises_router
from app.routers.estados import estados_router
from app.routers.regioes import regioes_router

from fastapi import FastAPI

app = FastAPI()
app.mount(path="/api", app=app)

app.include_router(paises_router, prefix='/paises', tags=['paises'])
app.include_router(estados_router, prefix='/estados', tags=['estados'])
app.include_router(regioes_router, prefix='/regioes', tags=['regioes'])
