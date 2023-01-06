import mysql.connector

def conexao():
    con = mysql.connector.connect(host="sql184.main-hosting.eu", user="u115428721_matheusDevTech", password="1010vcvC@!", database="u115428721_DB_matheusTech") 
    return con

def PegarUltimoValor():
    con = conexao()
    cur=con.cursor()
    cur.execute("SELECT * FROM precos ORDER BY created_date DESC LIMIT 1")
    res = cur.fetchall()
    cur.close()
    con.commit()
    con.close()
    return res

def EnviarUltimoValor(precos):
    con = conexao()
    cur=con.cursor()
    dolarParaReal = precos.dolarParaReal * 10000
    realParaDolar = precos.realParaDolar * 10000
    euroParaReal = precos.euroParaReal * 10000 
    realParaEuro = precos.realParaEuro * 10000
    euroParaDolar = precos.euroParaDolar * 10000
    dolarParaEuro = precos.dolarParaEuro * 10000

    query = """INSERT INTO precos (USD_BRL, BRL_USD, EUR_BRL, BRL_EUR, EUR_USD, USD_EUR) VALUES('%i','%i','%i','%i','%i','%i' )""" % (dolarParaReal,realParaDolar, euroParaReal, realParaEuro, euroParaDolar, dolarParaEuro)
    print( query)
        
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