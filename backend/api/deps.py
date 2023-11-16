from typing import Generator
from backend.db.session import ScopedSessionLocal


def get_db() -> Generator:
    db = ScopedSessionLocal()
    try:
        yield db
    finally:
        db.close()
