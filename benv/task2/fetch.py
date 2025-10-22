from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import uvicorn
import os
from typing import Optional

load_dotenv()

app = FastAPI(title="Simple FastAPI App", version="1.0.0")

data = [
    {"name": "Mulero Reuben", "age": 24, "track": "AI Developer"},
    {"name": "Grace Ade", "age": 21, "track": "Backend Developer"},
    {"name": "Jide Owolabi", "age": 22, "track": "Frontend Developer"}
]


class Item(BaseModel):
    name: str = Field(..., example="Perpetual")
    age: int = Field(..., example=25)
    track: str = Field(..., example="Fullstack Developer")


@app.get("/")
def root():
    return {"Message": "Welcome to my FastAPI Application"}


@app.get("/get-data")
def get_data():
    return data


@app.post("/create-data")
def create_data(req: Item):
    data.append(req.dict())
    return {"Message": "Data Received", "Data": data}


@app.put("/update-data/{id}")
def update_data(id: int, req: Item):
    if id < 0 or id >= len(data):
        return {"Error": "Data not found!"}
    data[id] = req.dict()
    return {"Message": "Data Updated", "Data": data}


@app.delete("/delete-data/{id}")
def delete_data(id: int):
    if id < 0 or id >= len(data):
        return {"Error": "Data not found!"}
    deleted_item = data.pop(id)
    return {"Message": "Record deleted successfully", "Deleted Data": deleted_item, "Remaining": data}


@app.patch("/update-info/{id}")
def update_info(
    id: int,
    name: Optional[str] = None,
    age: Optional[int] = None,
    track: Optional[str] = None
):
    if id < 0 or id >= len(data):
        return {"Error": "Data not found!"}

    if name is not None:
        data[id]["name"] = name
    if age is not None:
        data[id]["age"] = age
    if track is not None:
        data[id]["track"] = track

    return {"Message": "Data updated successfully", "Updated Data": data[id]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
