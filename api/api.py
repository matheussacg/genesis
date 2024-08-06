from fastapi import APIRouter
from v1.endpoints import usuario

api_router = APIRouter()
api_router.include_router(usuario.router, prefix="/usuario", tags=["usuario"])
