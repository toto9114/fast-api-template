from pydantic import BaseModel
from datetime import datetime
from datetime import datetime

from pydantic import BaseModel


class PlaceBase(BaseModel):
    owner_id: int
    name: str
    contents: str | None
    latitude: float | None
    longitude: float | None
    score: int


class PlaceCreate(PlaceBase):
    latitude: float
    longitude: float


class PlaceUpdate(PlaceBase):
    contents: str


class PlaceInDBBase(PlaceBase):
    id: int
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True


class Place(PlaceInDBBase):
    pass


class PlaceInDB(PlaceInDBBase):
    pass
