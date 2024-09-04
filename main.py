from enum import Enum

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from azure_blob import get_blob_service_client

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

blob_service_client = get_blob_service_client()



@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": "This is an item"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello, World!"}

@app.get("/containers")
async def read_root():
    containers = blob_service_client.list_containers()
    container_names = [container['name'] for container in containers]
    return {"containers": container_names}


@app.post("/upload-video/")
async def upload_video(file: UploadFile = File(...)):
    # Blob container'ı seçin veya oluşturun
    container_name = "videos"
    container_client = blob_service_client.get_container_client(container_name)

    # Eğer container mevcut değilse oluşturun
    if not container_client.exists():
        container_client.create_container()

    # Dosyayı blob olarak yükleyin
    blob_client = container_client.get_blob_client(file.filename)
    blob_client.upload_blob(file.file, blob_type="BlockBlob")

    return {"filename": file.filename, "status": "uploaded"}