# BIBLIOTECAS
from datetime import datetime
from pytz import timezone

# MODELS
from api.model.getDados import MD_getMinuto
from api.model.postIndex import postIndex

# ============================= POST =============================

def postIndex(dados):
    response = postIndex(dados)
    return {'status': response}

# ============================= GET =============================

def getMinuto():
    precos = MD_getMinuto()
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
