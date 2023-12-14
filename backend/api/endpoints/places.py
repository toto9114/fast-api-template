from typing import Any

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from backend import crud
from backend.api import deps
from backend.schemas.resp import CommonResponse

router = APIRouter()


@router.get("/", response_model=CommonResponse.schema(), status_code=status.HTTP_200_OK)
async def get_user_places(current_user: deps.CurrentUser, db: deps.SessionDep) -> Any:
    places = await crud.place.get_places(db=db, user_id=current_user.id)
    return CommonResponse(status_code=status.HTTP_200_OK, data=places)
