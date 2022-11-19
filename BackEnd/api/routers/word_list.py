from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/word_list")
async def get_word_list():
    pass

@router.post("/word_list")
async def create_word():
    pass

@router.put("/word_list")
async def update_word():
    pass

@router.delete("/word_list")
async def delete_word():
    pass