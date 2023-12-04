from backend.crud.base import CRUDBase
from backend.models.place import Place
from backend.schemas.place import PlaceCreate, PlaceUpdate
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDPlace(CRUDBase[Place, PlaceCreate, PlaceUpdate]):
    async def get_places(self, db: AsyncSession) -> list[Place]:
        query = select(self.model)
        result = await db.execute(query)

        return result.scalars().all()


place = CRUDPlace(Place)
