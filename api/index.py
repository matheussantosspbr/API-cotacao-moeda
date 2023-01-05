#!/usr/bin/env python3

from fastapi import FastAPI

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
