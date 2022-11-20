from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.db import get_db
import api.schemas.word as word_schema
import api.cruds.word as word_crud

router = APIRouter()

@router.get("/word_list", response_model=List[word_schema.Word])
async def get_word_list(db: AsyncSession = Depends(get_db)):
    return await word_crud.get_all_word(db)

@router.post("/word_list", response_model=word_schema.WordCreateResponse)
async def create_word(word_data: word_schema.WordCreate, db: AsyncSession = Depends(get_db)):
    return await word_crud.create_word(db, word_data)

@router.put("/word_list/{word_id}", response_model=word_schema.WordCreateResponse)
async def update_word(word_id: int, word_data: word_schema.WordCreate, db: AsyncSession = Depends(get_db)):
    word = await word_crud.get_word(db, word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")

    return await word_crud.update_word(db, word_id, word_data)

@router.delete("/word_list/{word_id}", response_model=None)
async def delete_word(word_id: int, db: AsyncSession = Depends(get_db)):
    word = await word_crud.get_word(db, word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")

    return await word_crud.delete_word(db, word_id)

@router.get("/word_list/set", response_model=List[word_schema.Word])
async def get_word_list_set(word_num:int =5, word_level:int = -1, db: AsyncSession = Depends(get_db)):
    all_words = await word_crud.get_all_word(db)
    # word_numの数だけランダムに単語を取得
    import random
    word_list = random.sample(all_words, word_num)
    return word_list