#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from conexao import PegarUltimoValor,EnviarUltimoValor
from api.conexao import PegarUltimoValor,EnviarUltimoValor

class require(BaseModel):
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
    

@app.post("/enviar/preco")
async def main(require: require):
    response = EnviarUltimoValor(require)
    return {'status': response}



@app.get("/")
async def home():
    precos = PegarUltimoValor()
    return {
        "USD_BRL":precos[0][1] / 100000,
        "BRL_USD":precos[0][2] / 100000,
        "EUR_BRL":precos[0][3]  / 100000,
        "BRL_EUR":precos[0][4]  / 100000,
        "EUR_USD":precos[0][5] / 100000,
        "USD_EUR":precos[0][6] / 100000,
        #"updated_at": str(precos[0][7]).replace('T', ' ')
        "updated_at": type(precos[0][7])
    }
