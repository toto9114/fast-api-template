from datetime import datetime, timedelta
from typing import Union, Any
from passlib.context import CryptContext
from jose import jwt
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


async def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    curr_time = datetime.utcnow()

    if expires_delta:
        expire = curr_time + expires_delta
    else:
        expire = curr_time + timedelta(minutes=settings.JWT_EXPIRE_MINUTE)
    to_encode = {"iat": curr_time, "exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


async def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
