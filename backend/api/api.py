from fastapi import APIRouter
from backend.api.endpoints import login, places, user

api_router = APIRouter(prefix="/api")

api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(places.router, prefix="/places", tags=["places"])
