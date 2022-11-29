from sqlalchemy import select
from sqlalchemy.engine import Result
from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
import api.models.word as word_model
import api.schemas.word as word_schema


def get_all_word(db: Session) -> List[word_model.Word]:
    result = db.query(word_model.Word).all()
    return result


# ↓未完成、エラーが出る
def get_all_word_of_level_N(db: Session, level_num: int) -> List[word_model.Word]:
    result = db.query(word_model.Word).filter(word_model.Wrod.level == level_num).all()
    return result


def create_word(db: Session, word_create: word_schema.WordCreate) -> word_schema.Word:
    word = word_model.Word(**word_create.dict())
    db.add(word)
    db.commit()
    db.refresh(word)
    return word


def get_word(db: Session, word_id: int) -> Optional[word_model.Word]:
    result: Result = db.query(word_model.Word).filter(word_model.Word.id == word_id)
    word: Optional[Tuple[word_model.Word]] = result.first()
    return word if word else None


def update_word(
    db: Session, word_id: int, word_data: word_schema.WordCreate
) -> word_schema.Word:
    word = db.get(word_model.Word, word_id)
    word.English_word = word_data.English_word
    word.Japanese_word = word_data.Japanese_word
    word.level = word_data.level
    db.commit()
    db.refresh(word)
    return word


def delete_word(db: Session, word_id: int) -> None:
    word = db.get(word_model.Word, word_id)
    db.delete(word)
    db.commit()
    return
