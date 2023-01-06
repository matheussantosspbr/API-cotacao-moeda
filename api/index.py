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
        "dolarParaReal":precos[0][1] / 100000,
        "realParaDolar":precos[0][2] / 100000,
        "euroParaReal":precos[0][3]  / 100000,
        "realParaEuro":precos[0][4]  / 100000,
        "euroParaDolar":precos[0][5] / 100000,
        "dolarParaEuro":precos[0][6] / 100000
    }
