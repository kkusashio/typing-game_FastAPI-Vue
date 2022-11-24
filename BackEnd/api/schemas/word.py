from typing import Optional

from pydantic import BaseModel, Field

class Word(BaseModel):
    id: int
    English_word: str = Field(...,  example="hello", description="英単語")
    Japanese_word: str = Field(...,example="こんにちは", description="日本語訳")
    level: int = Field(..., ge=1, example=1, description="英単語のレベル")

class WordCreate(BaseModel):
    English_word: str = Field(..., example="hello", description="英単語")
    Japanese_word: str = Field(..., example="こんにちは", description="日本語訳")
    level: int = Field(..., ge=1, example=1, description="英単語のレベル")

class WordCreateResponse(WordCreate):
    id: int

    class Config:
        orm_mode = True
