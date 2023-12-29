from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    ...


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    name: str
    created_at: datetime

    class Config:
        orm_mode = True