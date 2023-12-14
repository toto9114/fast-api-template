from typing import Annotated

from backend import crud
from backend import models
from backend.core.config import settings
from backend.db.session import AsyncScopedSessionLocal
from backend.schemas import TokenPayload
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession


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


SessionDep = Annotated[AsyncSession, Depends(get_db)]


async def get_current_user(
    db: AsyncSession = Depends(get_db),
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="token")),
) -> models.User:
    try:
        _parsed_access_token = jwt.decode(
            token, settings.JWT_SECRET, algorithms=settings.JWT_ALGORITHM
        )
        parsed_access_token = TokenPayload.model_validate(_parsed_access_token)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    user_id = parsed_access_token.sub
    user = await crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


CurrentUser = Annotated[models.User, Depends(get_current_user)]
