from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.engine import Result
from typing import List, Optional, Tuple
from passlib.context import CryptContext
from typing import Union
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import api.models.user as user_model
import api.schemas.user as user_schema
from api.db import get_db
from passlib import hash
import api.cruds.word as user_crud

# 本当は環境変数などに隠す？
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Userのリストを返す関数
def get_users(db, skip: int = 0, limit: int = 100):
    result = db.query(user_model.User).offset(skip).limit(limit).all()
    print(result)
    return result



# Userを登録する関数
def create_user(db: Session, user: user_schema.UserCreate):
    db_user = user_model.User(
        email=user.email,
        hashed_password=hash.bcrypt.hash(user.password),
        username=user.username,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Userをemailから取得する関数
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    result = db.query(user_model.User).filter(user_model.User.email == email).first()
    return result


# Userをusernameから取得する関数
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    result = (
        db.query(user_model.User).filter(user_model.User.username == username).first()
    )
    return result


# パスワードとハッシュ化パスワードを確かめる関数
def verify_password(plain_password, hashed_password) -> bool:
    return hash.bcrypt.verify(plain_password, hashed_password)


# ハッシュ化する関数
def get_password_hash(password):
    return hash.bcrypt.hash(password)


# usernameとパスワードからユーザーを返す関数
def authenticate_user(
    db: Session,
    username: str,
    password: str,
):
    user = get_user_by_username(username,db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return user_schema.UserInDB(**user_dict)

# アクセストークンを返す関数
def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# 現在のユーザを返す関数
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = user_schema.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(username=token_data.username,db=db)
    if user is None:
        raise credentials_exception
    return user


# def get_current_active_user(current_user: user_schema.User = Depends(get_current_user)):
#     print(current_user.disabled)
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user

# 　WIP
def update_word_for_user(
    db: Session,
    word_id: int,
    current_user: user_schema.User,
):
    # print("db",db)
    # word=user_crud.get_word(db,1)
    selected_words=current_user.words
    # selected_words = current_user.words
    return selected_words
