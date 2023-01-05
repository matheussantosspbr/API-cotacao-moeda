#!/usr/bin/env python3
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
        
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
    allow_origins=['*'],
)


@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/")
async def main():
    return {
        "name": "matheus",
        "idade": 18,
        "sexo": "M",
        "cidade": "Mauá",

    }
