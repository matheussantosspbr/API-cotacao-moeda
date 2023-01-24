#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from api.controller.controller import getNow, postIndex, RobotHourController, getDay



class postDado(BaseModel):
    secret_token: str
    public_token: str
    precos: dict
    
class token(BaseModel):
    secret_token: str
    public_token: str
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
    allow_origins=['https://precohoje.info', 'http://localhost:5173']

)
    
# ======================= INDEX =======================

@app.get("/")
async def index():
    return ''

# ======================= ROBOT =======================

@app.put("/bot/hour/active")
async def RobotHour(token: token):
    return RobotHourController(token)

# ======================= GET =======================

@app.get("/agora")
async def now():
    return getNow()

@app.get('/dia')
async def day():
    return getDay()

# ======================= POST =======================

@app.post("/post/preco/agora")
async def indexPost(postDado: postDado):
    return postIndex(postDado)




