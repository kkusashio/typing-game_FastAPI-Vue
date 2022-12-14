from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base
from api.models.user_word_map import UserWordMap


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    English_word = Column(String(50), nullable=False)
    Japanese_word = Column(String(50), nullable=False)
    level = Column(Integer, nullable=False)
    users = relationship(
        "User", secondary=UserWordMap.__tablename__, back_populates="words"
    )
