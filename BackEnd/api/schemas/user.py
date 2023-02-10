from pydantic import BaseModel, Field
from typing import Union, List
from api.schemas.word import Word


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class UserBase(BaseModel):
    pass
    # email: str


class UserCreate(UserBase):
    username: str
    password: str


class User(UserBase):
    id: int
    username: str
    is_active: bool
    rate: int
    words: List[Word] = []

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
