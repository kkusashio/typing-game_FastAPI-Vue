from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from typing import List, Optional,Tuple

import api.models.word as word_model
import api.schemas.word as word_schema


async def get_all_word(db: AsyncSession) -> List[word_model.Word]:
    result= await db.execute(word_model.Word.__table__.select())
    print(result)
    return result.all()

async def create_word(
    db: AsyncSession, word_create: word_schema.WordCreate
) -> word_schema.Word:
    word = word_model.Word(**word_create.dict())
    db.add(word)
    await db.commit()
    await db.refresh(word)
    return word

async def get_word(db: AsyncSession, word_id: int) -> Optional[word_model.Word]:
    result: Result = await db.execute(
        select(word_model.Word).filter(word_model.Word.id == word_id)
    )
    word: Optional[Tuple[word_model.Word]] = result.first()
    return word[0] if word else None

async def update_word(
    db: AsyncSession, word_id: int, word_data: word_schema.WordCreate
) -> word_schema.Word:
    word = await db.get(word_model.Word, word_id)
    word.English_word = word_data.English_word
    word.Japanese_word = word_data.Japanese_word
    word.level = word_data.level
    await db.commit()
    await db.refresh(word)
    return word

async def delete_word(db: AsyncSession, word_id: int) -> None:
    word = await db.get(word_model.Word, word_id)
    await db.delete(word)
    await db.commit()
    return
