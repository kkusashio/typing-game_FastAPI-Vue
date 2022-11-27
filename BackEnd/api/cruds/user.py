from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from typing import List, Optional,Tuple
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

# 本当は環境変数などに隠す？
SECRET_KEY = "45d7a739ed783dba4638091687c49224dc1a9fc56d91135490094f2d9ac53869"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Userのリストを返す関数
async def get_users(db,skip:int=0,limit:int=100):
    result= await db.execute(user_model.User.__table__.select().offset(skip).limit(limit))
    return result.all()

# Userを登録する関数
async def create_user(db: AsyncSession,user:user_schema.UserCreate):
    db_user=user_model.User(email=user.email,hashed_password=hash.bcrypt.hash(user.password),username=user.username)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# Userをemailから取得する関数
async def get_user_by_email(db, email: str):
    result =await db.execute(
        user_model.User.__table__.select().filter(user_model.User.email == email)
        # select(user_model.User).filter(user_model.User.email == email)
    )
    result = result.first()
    return result

# Userをusernameから取得する関数
async def get_user_by_username(db, username: str):
    result = await db.execute(
        user_model.User.__table__.select().filter(user_model.User.username == username)
    )
    return result.first()

# パスワードとハッシュ化パスワードを確かめる関数
def verify_password(plain_password, hashed_password)->bool:
    return hash.bcrypt.verify(plain_password, hashed_password)

# ハッシュ化する関数
def get_password_hash(password):
    return hash.bcrypt.hash(password)

# usernameとパスワードからユーザーを返す関数  
async def authenticate_user(
        db: AsyncSession,
        username: str,
        password: str,
        ):
    user = await get_user_by_username(db, username)
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
async def get_current_user(token: str = Depends(oauth2_scheme),db:AsyncSession=Depends(get_db)):
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
    user = get_user_by_email(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# async def get_current_active_user(current_user: user_schema.User = Depends(get_current_user)):
#     print(current_user.disabled)
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user