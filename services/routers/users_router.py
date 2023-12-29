from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.datebase import get_db

from models.schemas import user

from typing import List

from repositories import users as repositories_users

APIRouterUser = APIRouter()

@APIRouterUser.get("/", response_model=List[user.User])
async def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return repositories_users.get_users(db=db, skip=skip, limit=limit)