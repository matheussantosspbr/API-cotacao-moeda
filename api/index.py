#!/usr/bin/env python3
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
        
app = FastAPI()


@app.get('/api/hello')
async def hello():
    return {'message': 'Hello world!!'}

@app.get("/")
async def main():
    return {
        "name": "matheus",
        "idade": 18,
        "sexo": "M",
        "cidade": "Mauá",

    }

@app.post("/items")
async def create_item(item: Item):
    return item
