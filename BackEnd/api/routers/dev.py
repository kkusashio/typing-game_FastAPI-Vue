from typing import List
import random
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.db import get_db
import api.schemas.word as word_schema
import api.cruds.word as word_crud

router = APIRouter()

@router.delete("/dev/init_db", response_model=None)
async def init_db():
    try:
        from api.models.word import Base
        from sqlalchemy import create_engine

        DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
        engine = create_engine(DB_URL, echo=True)
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

