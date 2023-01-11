import mysql.connector
from api.token import secret_token, public_token
import pytz
from datetime import datetime, timezone

myTimezone = pytz.timezone('America/Sao_Paulo')

def conexao():
    con = mysql.connector.connect(host="sql184.main-hosting.eu", user="u115428721_matheusDevTech", password="1010vcvC@!", database="u115428721_DB_matheusTech") 
    return con

def PegarUltimoValor():
    con = conexao()
    cur = con.cursor()
    cur.execute("SELECT * FROM precos WHERE id = 1")
    res = cur.fetchall()
    cur.close()
    con.commit()
    con.close()
    return res

def EnviarUltimoValor(data):
    if data.secret_token == secret_token and data.public_token == public_token:
        con = conexao()
        cur = con.cursor()
        dolarParaReal = data.precos['dolarParaReal'] * 100000
        realParaDolar = data.precos['realParaDolar'] * 100000
        euroParaReal = data.precos['euroParaReal'] * 100000
        realParaEuro = data.precos['realParaEuro'] * 100000
        euroParaDolar = data.precos['euroParaDolar'] * 100000
        dolarParaEuro = data.precos['dolarParaEuro'] * 100000

        # Timestamp
        data_hora_padrão = datetime.now()
        timestamp_padrão = datetime.timestamp(data_hora_padrão)
        myData_hora = datetime.now(myTimezone)
        myTimestamp = datetime.timestamp(myData_hora)
        myData_hora_formatada = datetime.utcfromtimestamp(int(myTimestamp)).strftime('%d/%m/%Y %H:%m:%S')
        
        query = """
            UPDATE precos
            SET USD_BRL = '%i', BRL_USD = '%i', EUR_BRL = '%i', BRL_EUR = '%i', EUR_USD = '%i', USD_EUR = '%i', timestamp = '%i', updated_at = '%s'
            WHERE id = 1;
        """ % (dolarParaReal,realParaDolar, euroParaReal, realParaEuro, euroParaDolar, dolarParaEuro, int(timestamp_padrão),str(myData_hora_formatada),)
            
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
    else:
        return {
           'status': 503,
           'message': 'Token inválido'
        }