from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from uuid import uuid4

app = FastAPI(
    title="Simple CRUD API",
    description="A simple CRUD API without a database using FastAPI",
    version="1.0.0"
)

# In-memory storage
items_db = {}

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    price: float = Field(..., gt=0)
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Laptop",
                "description": "A high-performance laptop",
                "price": 999.99
            }
        }

class Item(ItemCreate):
    id: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "Laptop",
                "description": "A high-performance laptop",
                "price": 999.99
            }
        }

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Simple CRUD API"}

@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(item: ItemCreate):
    """
    Create a new item with the given details
    """
    item_id = str(uuid4())
    items_db[item_id] = Item(id=item_id, **item.dict())
    return items_db[item_id]

@app.get("/items/", response_model=List[Item], tags=["Items"])
def read_items():
    """
    Get all items
    """
    return list(items_db.values())

@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def read_item(item_id: str):
    """
    Get a specific item by ID
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
def update_item(item_id: str, item: ItemCreate):
    """
    Update an existing item
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    items_db[item_id] = Item(id=item_id, **item.dict())
    return items_db[item_id]

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: str):
    """
    Delete an item
    """
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    del items_db[item_id]
    return None