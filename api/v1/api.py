from fastapi import APIRouter
from api.v1.endpoints import usuario


api_router = APIRouter()
api_router.include_router(usuario.router, prefix="/usuario", tags=["usuario"])
