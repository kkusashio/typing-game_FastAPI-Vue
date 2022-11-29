from typing import List
import random
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.db import get_db
import api.schemas.word as word_schema
import api.cruds.word as word_crud

router = APIRouter()


@router.get("/word_list", response_model=List[word_schema.Word])
def get_word_list(db: Session = Depends(get_db)):
    result=word_crud.get_all_word(db)
    return result


@router.post("/word_list", response_model=word_schema.WordCreateResponse)
def create_word(word_data: word_schema.WordCreate, db: Session = Depends(get_db)):
    return word_crud.create_word(db, word_data)


@router.put("/word_list/{word_id}", response_model=word_schema.WordCreateResponse)
def update_word(
    word_id: int, word_data: word_schema.WordCreate, db: Session = Depends(get_db)
):
    word = word_crud.get_word(db, word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")

    return word_crud.update_word(db, word_id, word_data)


@router.delete("/word_list/{word_id}", response_model=None)
def delete_word(word_id: int, db: Session = Depends(get_db)):
    word = word_crud.get_word(db, word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")

    return word_crud.delete_word(db, word_id)


@router.get("/word_list/set", response_model=List[word_schema.Word])
def get_word_list_set(
    word_num: int = 5, word_level: int = -1, db: Session = Depends(get_db)
):

    # レベルの指定がない場合、全ての単語を対象とする
    if word_level == -1:
        all_words = word_crud.get_all_word(db)
    else:
        # ↓未完成、エラーが出る
        all_words = word_crud.get_all_word_of_level_N(db, word_level)

    # 単語数が単語リストの数より多い場合、単語リストの数を単語数とする
    if word_num > len(all_words):
        word_num = len(all_words)

    # 単語リストから単語数分の単語をランダムに選択する
    word_list = random.sample(all_words, word_num)
    return word_list
