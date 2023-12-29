from pydantic import BaseModel
from .user import User


class ItemBase(BaseModel):
   ...


class ItemCreate(ItemBase):
    ...


class Item(ItemBase):
    id: int
    owner_id: int

    item: User = None

    class Config:
        orm_mode = True