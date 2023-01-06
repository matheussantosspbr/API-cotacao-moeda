#!/usr/bin/env python3
from fastapi import FastAPI
# from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from conexao import PegarUltimoValor

# class PropsPrecos(BaseModel):
#     dolarParaReal: float
#     realParaDolar: float
#     euroParaReal: float
#     realParaEuro: float
#     euroParaDolar: float
#     dolarParaEuro: float
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True,
    allow_origins=['*'],
)
    

# @app.post("/enviar/preco")
# async def main(precos: PropsPrecos):
#     status = EnviarUltimoValor(precos)
#     return {'status': status}



@app.get("/")
async def home():
    precos = PegarUltimoValor()
    return {
        "dolarParaReal":precos[0][1] / 10000,
        "realParaDolar":precos[0][2] / 10000,
        "euroParaReal":precos[0][3]  / 10000,
        "realParaEuro":precos[0][4]  / 10000,
        "euroParaDolar":precos[0][5] / 10000,
        "dolarParaEuro":precos[0][6] / 10000
    }
