from typing import Optional, Union, List
from typing import Union, List, Any
from pydantic import BaseModel, Field

# from api.schemas.user import User


class WordCreate(BaseModel):
    English_word: str = Field(..., example="hello", description="英単語")
    Japanese_word: str = Field(..., example="こんにちは", description="日本語訳")
    level: int = Field(..., ge=1, example=1, description="英単語のレベル")
    owner_id: Union[None, int] = Field(..., example=0, description="単語登録者のID")


class WordCreateResponse(WordCreate):
    id: int

    class Config:
        orm_mode = True


class Word(WordCreateResponse):
    id: int
    English_word: str = Field(..., example="hello", description="英単語")
    Japanese_word: str = Field(..., example="こんにちは", description="日本語訳")
    level: int = Field(..., ge=1, example=1, description="英単語のレベル")


class WordPost(BaseModel):
    word_id: int
