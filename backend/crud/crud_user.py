from typing import Optional

from backend.core.security import get_password_hash, verify_password
from backend.crud.base import CRUDBase
from backend.models.user import User
from backend.schemas.user import UserCreate, UserUpdate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_by_email(self, db: AsyncSession, *, email: str) -> Optional[User]:
        query = select(self.model).where(User.email == email)
        result = await db.execute(query)
        return result.scalar_one_or_none()

    async def create(self, db: AsyncSession, obj_in: UserCreate) -> User:
        db_obj = User(
            email=obj_in.email,
            hashed_password=await get_password_hash(obj_in.password),
            is_superuser=obj_in.is_superuser,
        )
        db.add(db_obj)
        # await db.refresh(db_obj)
        return db_obj

    async def authenticate(
        self, db: AsyncSession, *, email: str, password: str
    ) -> Optional[User]:
        user = await self.get_by_email(db, email=email)
        if not user:
            return None
        if not await verify_password(password, user.hashed_password):
            return None
        return user

    async def is_active(self, user: User) -> bool:
        return user.is_active

    async def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)
