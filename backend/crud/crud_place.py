from typing import List
from sqlalchemy.orm import Session
from backend.crud.base import CRUDBase
from backend.models.place import Place
from backend.schemas.place import PlaceCreate, PlaceUpdate


class CRUDPlace(CRUDBase[Place, PlaceCreate, PlaceUpdate]):
    def get_places(self, db: Session) -> List[Place]:
        queryset = db.query(self.model).limit(100).all()
        return queryset


place = CRUDPlace(Place)
