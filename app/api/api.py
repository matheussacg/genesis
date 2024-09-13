from fastapi import APIRouter, Response

from app.api.v1.endpoints import user
import prometheus_client

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])


@api_router.get("/metrics")
async def metrics():
    return Response(
        media_type="text/plain",
        content=prometheus_client.generate_latest(),
    )

