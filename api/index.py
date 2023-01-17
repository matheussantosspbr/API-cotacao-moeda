#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from api.controller.controller import getMinuto, indexPost


class postDado(BaseModel):
    secret_token: str
    public_token: str
    precos: dict
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
    allow_origins=['*'],
)
    
# ======================= INDEX =======================

@app.get("/")
async def index():
    return ''

# ======================= GET =======================

@app.get("/agora")
async def now():
    return getMinuto()

# ======================= POST =======================

@app.post("/POST/preco/agora")
async def indexPost(postDado: postDado):
    return indexPost(postDado)




