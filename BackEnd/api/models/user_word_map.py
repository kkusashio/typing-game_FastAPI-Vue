from sqlalchemy import Boolean, Column, Integer, String,ForeignKey,Table
from sqlalchemy.orm import relationship
# from pydantic import EmailStr, constr
from api.db import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# 参考
# https://muoilog.xyz/web-development/sqlalchemy-many-to-many-save/
# user_word_map_table=Table(
#     "user_word_map",
#     Base.metadata,
#     Column('user_id',Integer,ForeignKey("users.id"),primary_key=True),
#     Column('word_id',Integer,ForeignKey("words.id"),primary_key=True)
# )
class UserWordMap(Base):
    __tablename__='user_word_map'
    user_id=Column('user_id',Integer,ForeignKey("users.id"),primary_key=True)
    word_id=Column('word_id',Integer,ForeignKey("words.id"),primary_key=True)
