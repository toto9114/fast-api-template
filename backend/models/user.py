from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func, text
from sqlalchemy.orm import relationship

from backend.db.base_class import Base

if TYPE_CHECKING:
    from .place import Place


class User(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(20), unique=True, index=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now())
    places = relationship("Place", back_populates="owner")
