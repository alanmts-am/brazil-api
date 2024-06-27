from app.routers.paises import paises_router
from app.routers.estados import estado_router
from app.routers.regioes import regiao_router
from app.routers.municipios import municipio_router

from fastapi import FastAPI

app = FastAPI()
app.mount(path="/api", app=app)

app.include_router(paises_router, prefix='/paises', tags=['paises'])
app.include_router(estado_router, prefix='/estados', tags=['estados'])
app.include_router(regiao_router, prefix='/regioes', tags=['regioes'])
app.include_router(municipio_router, prefix='/municipios',
                   tags=['municipios'])
