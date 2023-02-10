from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

# from pydantic import EmailStr, constr
from api.db import Base
from api.models.user_word_map import UserWordMap


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # email = Column(String(254), unique=True, index=True)
    username = Column(String(128), unique=True, index=True)
    hashed_password = Column(String(128))
    is_active = Column(Boolean, default=True)
    rate = Column(Integer, default=1000)
    words = relationship(
        "Word", secondary=UserWordMap.__tablename__, back_populates="users"
    )
