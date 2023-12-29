from fastapi import APIRouter

APIRouterItem = APIRouter()

@APIRouterItem.get("/")
async def get_items():
    return {"message": "Hello World"}

@APIRouterItem.get("/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}