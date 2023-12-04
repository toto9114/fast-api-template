from typing import Generator
from backend.db.session import AsyncScopedSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


async def get_db() -> AsyncSession:
    # session = AsyncScopedSessionLocal()
    async with AsyncScopedSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
