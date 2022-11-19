from typing import List
from fastapi import APIRouter, Depends, HTTPException

import api.schemas.word as word_schema

router = APIRouter()

@router.get("/word_list", response_model=List[word_schema.Word])
async def get_word_list():
    return [word_schema.Word(id=1, English_word="hello", Japanese_word="こんにちは", level=1),word_schema.Word(id=2, English_word="goodbye", Japanese_word="さようなら", level=2)]

@router.post("/word_list", response_model=word_schema.Word)
async def create_word(word_data: word_schema.WordCreate):
    return word_schema.Word(id=1, **word_data.dict())

@router.put("/word_list/{word_id}", response_model=word_schema.Word)
async def update_word(word_id: int, word_data: word_schema.WordCreate):
    return word_schema.Word(id=word_id, **word_data.dict())

@router.delete("/word_list/{word_id}", response_model=None)
async def delete_word(word_id: int):
    return