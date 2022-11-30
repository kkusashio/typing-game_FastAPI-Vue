from fastapi import FastAPI
from api.routers import word_list,user
from api.routers import dev

app = FastAPI()

app.include_router(word_list.router)
app.include_router(dev.router)
app.include_router(user.router)