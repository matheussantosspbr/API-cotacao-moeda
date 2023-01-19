# BIBLIOTECAS
from datetime import datetime
from pytz import timezone
import json

# MODELS
from api.model.getDados import MD_getNow, MD_getDay
from api.model.post_Index import post_Index

# ARQUIVOS
from api.controller.RobotController import RobotHour
from api.auth.validacao import validar

# ============================= ROBOT ===========================

def RobotHourController(token):
    token = [ token.secret_token, token.public_token]
    res = validar(token)
    
    if res['status'] == 200 and res['message'] == 'ok':
        return RobotHour(token)
    else:
        return res

# ============================= POST ============================

def postIndex(dados):
    token = [ dados.secret_token, dados.public_token]
    res = validar(token)
    
    if res['status'] == 200 and res['message'] == 'ok':
        return post_Index(dados)
    else:
        return res
    

# ============================= GET =============================

def getNow():
    precos = MD_getNow()
    timestamp = int(precos[0][7])
    myDatetime = datetime.fromtimestamp(timestamp, tz = timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M:%S') 
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

def getDay():
    precos = MD_getDay()
    dados = {}
    for preco in precos:
        dados.update({
            "USD_BRL": preco[1] / 100000,
            "BRL_USD": preco[2] / 100000,
            "EUR_BRL": preco[3] / 100000,
            "BRL_EUR": preco[4] / 100000,
            "EUR_USD": preco[5] / 100000,
            "USD_EUR": preco[6] / 100000,
            "timestamp":preco[7]
            }
        )
    json_str = json.dumps(dados)
    return {
        json.loads(json_str)
    }
