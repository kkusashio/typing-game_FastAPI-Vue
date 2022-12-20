from fastapi import FastAPI
from api.routers import word_list,user
from api.routers import dev
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins=[
    "http://localhost:8080",

]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(word_list.router)
app.include_router(dev.router)
app.include_router(user.router)