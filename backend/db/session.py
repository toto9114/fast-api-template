from contextvars import ContextVar

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from backend.core.config import settings

session_context: ContextVar[str] = ContextVar("session_context")


def get_session_context() -> str:
    return session_context.get()


engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
ScopedSessionLocal = scoped_session(SessionLocal, scopefunc=get_session_context)
