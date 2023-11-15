from fastapi import APIRouter
from backend.api.endpoints import places

api_router = APIRouter()

api_router.include_router(places.router, prefix="/places", tags=["places"])
