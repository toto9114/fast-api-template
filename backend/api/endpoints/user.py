from typing import List, Any
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from backend import schemas
from backend.schemas import CommonResponse, User
from backend.api import deps
from backend import crud

router = APIRouter()


@router.post(
    "/", response_model=CommonResponse.schema(), status_code=status.HTTP_201_CREATED
)
async def signup(*, db: deps.SessionDep, user_in: schemas.UserCreate) -> Any:
    await crud.user.create(db=db, obj_in=user_in)
    return CommonResponse(status_code=status.HTTP_201_CREATED)
