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
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": "This is an item"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello, World!"}