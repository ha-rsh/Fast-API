from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name : str
    brand : Optional[str] = None
    price : int

app = FastAPI()

inventory = {}
@app.get("/get-item/{item_id}")
def get_item(item_id : int = Path(None, description="The ID of the item you like to see")):
    if item_id not in inventory:
        return {"Data": "Not found"}
  
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: str = Query(None, title="Name", description="Name of the item")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]

    return {"Data": "Not Found"}

@app.post("/create-post/{item_id}")
def create_item(item_id:int, item:Item):
    if item_id in inventory:
        return {"Error": "Item already exists"}

    else:
        inventory[item_id] = item
        return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id:int = Query(..., description="The ID of the item to delete")):
    if item_id not in inventory:
        return {"Error" : "Item not in inventory"}

    del inventory[item_id]