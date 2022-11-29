from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from api.db import get_db
import api.schemas.user as user_schema
import api.cruds.user as user_crud
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from typing import List

ACCESS_TOKEN_EXPIRE_MINUTES = 30
router = APIRouter()

# ----------------GET-----------------#
# Userの一覧を取得（確認用）
@router.get("/users/", response_model=List[user_schema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    print(users)
    return users


# ---------------POST----------------
# usernameとpasswordでログイン
# frontendから呼び出すときの参考？
# https://qiita.com/sand/items/990afc5d49a37b026acc#2-3-vue%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%A0---indexjs
@router.post("/token", response_model=user_schema.Token)
def user_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = user_crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = user_crud.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = user_crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# 新しくユーザーを登録する
@router.post("/users/")
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(email=user.email,db=db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = user_crud.get_user_by_username(username=user.username,db=db)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = user_crud.create_user(db=db, user=user)
    access_token_expires = user_crud.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = user_crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=user_schema.User)
def read_users_me(
    current_user: user_schema.User = Depends(user_crud.get_current_user),
    db: Session = Depends(get_db),
):
    return current_user

@router.delete("/users/me/words", status_code=204)
def del_users_me_word(
    word_id:int,
    current_user: user_schema.User = Depends(user_crud.get_current_user),
    db: Session = Depends(get_db),
):
    user_crud.delete_word_for_user(db,word_id=word_id,current_user=current_user)

@router.post("/users/me/words", status_code=204)
def del_users_me_word(
    word_id:int,
    current_user: user_schema.User = Depends(user_crud.get_current_user),
    db: Session = Depends(get_db),
):
    user_crud.add_word_for_user(db,word_id=word_id,current_user=current_user)
# @router.get("/users/me/items/")
# async def read_own_items(current_user: user_schema.User = Depends(user_crud.get_current_active_user)):
#     return [{"item_id": "Foo", "owner": current_user.username}]
