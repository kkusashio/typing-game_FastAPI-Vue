from typing import List
import random
from fastapi import APIRouter, Depends, HTTPException

from api.db import get_db
import api.schemas.word as word_schema
import api.cruds.word as word_crud
from sqlalchemy.orm import Session


router = APIRouter()

from api.models.word import Base
from sqlalchemy import create_engine


@router.delete("/dev/init_db", response_model=None)
def init_db():
    try:
        from utils import reset_database

        reset_database()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


from fastapi import UploadFile, File


@router.post("/dev/upload_xmls", response_model=None)
def get_excel_file(upload_file: UploadFile = File(...)):
    try:
        # ファイルを/tmpに保存
        with open("/tmp/" + upload_file.filename, "wb") as f:
            f.write(upload_file.file.read())

        # ファイルを読み込んで、DBに登録
        from utils import add_word_from_xlsx

        add_word_from_xlsx("/tmp/" + upload_file.filename)

        return None
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
