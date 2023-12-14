from backend.crud.base import CRUDBase
from backend.models.place import Place
from backend.schemas.place import PlaceCreate, PlaceUpdate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDPlace(CRUDBase[Place, PlaceCreate, PlaceUpdate]):
    async def get_places(self, db: AsyncSession, user_id: str) -> list[Place]:
        query = select(self.model).where(self.model.owner_id == user_id)
        result = await db.execute(query)

        return result.scalars().all()


place = CRUDPlace(Place)
