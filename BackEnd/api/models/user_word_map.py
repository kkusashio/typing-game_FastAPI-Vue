from sqlalchemy import Boolean, Column, Integer, String,ForeignKey,Table
from sqlalchemy.orm import relationship
# from pydantic import EmailStr, constr
from api.db import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

user_word_map_table=Table(
    "user_word_map",
    Base.metadata,
    Column('user_id',Integer,ForeignKey("users.id")),
    Column('word_id',Integer,ForeignKey("words.id"))
)

