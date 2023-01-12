#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from conexao import PegarUltimoValor,EnviarUltimoValor
from api.conexao import PegarUltimoValor,EnviarUltimoValor
from datetime import datetime
import pytz


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
    timestamp = datetime.fromtimestamp(int(precos[0][7]))
    myTimezone = pytz.timezone('America/Sao_Paulo')
    myDatetime = datetime.fromtimestamp(timestamp,myTimezone).strftime('%d/%m/%Y %H:%M:%S')
    return {
        "USD_BRL":precos[0][1] / 100000,
        "BRL_USD":precos[0][2] / 100000,
        "EUR_BRL":precos[0][3] / 100000,
        "BRL_EUR":precos[0][4] / 100000,
        "EUR_USD":precos[0][5] / 100000,
        "USD_EUR":precos[0][6] / 100000,
        "timestamp":precos[0][7],
        "updated_at" : myDatetime
    }
