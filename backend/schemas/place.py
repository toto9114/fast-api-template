from typing import Optional
from pydantic import BaseModel


class PlaceBase(BaseModel):
    owner_id: int
    name: str
    content: str | None
    latitude: float | None
    longitude: float | None
    score: int


class PlaceCreate(PlaceBase):
    latitude = float
    longitude = float


class PlaceUpdate(PlaceBase):
    content = str


class PlaceInDBBase(PlaceBase):
    id: int
    created_at: str
    updated_at: str | None

    class Config:
        orm_mode = True


class Place(PlaceInDBBase):
    pass


class PlaceInDB(PlaceInDBBase):
    pass
