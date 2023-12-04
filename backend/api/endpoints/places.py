from typing import Any

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend import crud
from backend.api import deps
from backend.schemas.resp import CommonResponse

router = APIRouter()


@router.get("/", response_model=CommonResponse.schema(), status_code=status.HTTP_200_OK)
async def get_user_places(db: Session = Depends(deps.get_db)) -> Any:
    places = await crud.place.get_places(db=db)
    return CommonResponse(status_code=status.HTTP_200_OK, data=places)
