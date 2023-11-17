from contextvars import ContextVar, Token

from backend.core.config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, async_scoped_session

session_context: ContextVar[str] = ContextVar("session_context")


def get_session_context() -> str:
    return session_context.get()


def set_session_context(session_id: str) -> Token:
    return session_context.set(session_id)


def reset_session_context(context: Token) -> None:
    session_context.reset(context)


engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, pool_recycle=3600)
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False,
                                       class_=AsyncSession)
AsyncScopedSessionLocal = async_scoped_session(AsyncSessionLocal, scopefunc=get_session_context)
