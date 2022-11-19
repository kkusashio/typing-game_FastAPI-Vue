from fastapi import FastAPI
from api.routers import word_list

app = FastAPI()

app.include_router(word_list.router)

@app.get("/hello")
def read_root():
    return {"Hello": "World"}