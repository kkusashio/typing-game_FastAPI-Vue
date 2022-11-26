from fastapi import APIRouter,Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from api.db import get_db
import api.schemas.login as login_schema
import api.cruds.login as login_crud
from passlib.context import CryptContext

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}
@router.post("/token", response_model=login_schema.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = login_crud.authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = login_crud.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = login_crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=login_schema.User)
async def read_users_me(current_user: login_schema.User = Depends(login_crud.get_current_active_user)):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: login_schema.User = Depends(login_crud.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]