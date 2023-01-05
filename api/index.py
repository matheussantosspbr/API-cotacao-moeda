#!/usr/bin/env python3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

        
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
    allow_origins=['*'],
)


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
