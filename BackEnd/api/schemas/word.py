from typing import Optional

from pydantic import BaseModel, Field

class Word(BaseModel):
    id: int
    English_word: str = Field(..., regex=r"^[a-zA-Z]+$", example="hello", description="英単語")
    Japanese_word: str = Field(..., regex=r"^[ぁ-んァ-ン一-龥]+$", example="こんにちは", description="日本語訳")
    level: int = Field(..., ge=1, le=5, example=1, description="英単語のレベル")

class WordCreate(BaseModel):
    English_word: str = Field(..., regex=r"^[a-zA-Z]+$", example="hello", description="英単語")
    Japanese_word: str = Field(..., regex=r"^[ぁ-んァ-ン一-龥]+$", example="こんにちは", description="日本語訳")
    level: int = Field(..., ge=1, le=5, example=1, description="英単語のレベル")

    class Config:
        orm_mode = True

