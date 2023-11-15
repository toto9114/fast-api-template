from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String, Float, TIMESTAMP
from sqlalchemy.sql import func, text
from sqlalchemy.orm import relationship
from backend.db.base_class import Base

if TYPE_CHECKING:
    from .user import User


class Place(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(20), index=True)
    contents = Column(String(200), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    score = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="places")
