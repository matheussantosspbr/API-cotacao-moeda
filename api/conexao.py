import mysql.connector
from api.token import secret_token, public_token

def conexao():
    con = mysql.connector.connect(host="sql184.main-hosting.eu", user="u115428721_matheusDevTech", password="1010vcvC@!", database="u115428721_DB_matheusTech") 
    return con

def PegarUltimoValor():
    con = conexao()
    cur = con.cursor()
    cur.execute("SELECT * FROM precos ORDER BY created_date DESC LIMIT 1")
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

        query = """INSERT INTO precos (USD_BRL, BRL_USD, EUR_BRL, BRL_EUR, EUR_USD, USD_EUR) VALUES('%i','%i','%i','%i','%i','%i' )""" % (dolarParaReal,realParaDolar, euroParaReal, realParaEuro, euroParaDolar, dolarParaEuro)
        print(query)
            
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