# BIBLIOTECAS
from datetime import datetime
from pytz import timezone

from api.model.db.conexao import conexao

def SelectHour():
        
    con = conexao()
    cur = con.cursor()
    
    query = """
        SELECT 
            AVG(USD_BRL) as USD_BRL,
            AVG(BRL_USD) as BRL_USD,
            AVG(EUR_BRL) as EUR_BRL,
            AVG(BRL_EUR) as BRL_EUR,
            AVG(EUR_USD) as EUR_USD,
            AVG(USD_EUR) as USD_EUR
        FROM
            precos  
        WHERE
            HOUR(FROM_UNIXTIME(timestamp)) = HOUR(DATE_SUB(NOW(), INTERVAL 1 HOUR));
    """
    cur.execute(query)
    response = cur.fetchall()
    cur.close()
    con.commit()
    con.close()
    
    insert = InsertHour(response)
    if insert['status'] == 201:
        DeleteHour()
    else:
        return insert

def InsertHour(dado):
    con = conexao()
    cur = con.cursor()
    dolarParaReal = round((dado[0][0] / 100000), 2) * 100000
    realParaDolar = round((dado[0][1] / 100000), 2) * 100000
    euroParaReal = round((dado[0][2] / 100000), 2) * 100000
    realParaEuro = round((dado[0][3] / 100000), 2) * 100000
    euroParaDolar = round((dado[0][4] / 100000), 2) * 100000
    dolarParaEuro = round((dado[0][5] / 100000), 2) * 100000
    
    # Timestamp
    data_hora_padrão = datetime.now()
    timestamp_padrão = datetime.timestamp(data_hora_padrão)
    
    query = """INSERT INTO day
                    (USD_BRL, BRL_USD, EUR_BRL, BRL_EUR, EUR_USD, USD_EUR, timestamp)
               VALUES
                    ('%i','%i','%i','%i','%i','%i', '%i' )""" % (dolarParaReal,realParaDolar, euroParaReal, realParaEuro, euroParaDolar, dolarParaEuro, int(timestamp_padrão))
    try:
        cur.execute(query)
        cur.close()
        con.commit()
        con.close()
        return{
            'status': 201,
            'message':'Valor criado com sucesso'
        }
    except:
        cur.close()
        con.commit()
        con.close()
        
        return {
            'status': 400,
            'message': "Erro ao tentar enviar um valor"
        }

def DeleteHour():
    query = "DELETE FROM precos WHERE HOUR(FROM_UNIXTIME(timestamp)) = HOUR(DATE_SUB(NOW(), INTERVAL 1 HOUR));"
    
    con = conexao()
    cur = con.cursor()
    cur.execute(query)
    cur.close()
    con.commit()
    con.close()