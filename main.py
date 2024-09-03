from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Category(Enum):
    TOOLS = "tools"
    CONSUMABLES = "consumables"

class Item(BaseModel):
    name :str
    price: float
    count: int
    id: int
    category: Category

items = {
    0: Item(name="Hammer", price=9.99, count=20,id=0,category=Category.TOOLS)
}

@app.get("/")
def index() -> Dict[str, Dict[int, Item]]:
    return {"items": items}