from fastapi import APIRouter,Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@router.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}