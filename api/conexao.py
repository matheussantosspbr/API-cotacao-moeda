import mysql.connector

class BancoDeDados:
    def __init__(self):
        self.con = mysql.connector.connect(host="sql184.main-hosting.eu", user="u115428721_matheusDevTech", password="1010vcvC@!", database="u115428721_DB_matheusTech")
        

    def PegarUltimoValor(self):
        con = self.con
        db = con.cursor()
        db.execute("SELECT * FROM precos ORDER BY created_date DESC LIMIT 1")
        return db.fetchall()

    def EnviarUltimoValor(precos,self):
        con = self.con
        db=con.cursor()
        dolarParaReal = precos.dolarParaReal * 10000
        realParaDolar = precos.realParaDolar * 10000
        euroParaReal = precos.euroParaReal * 10000 
        realParaEuro = precos.realParaEuro * 10000
        euroParaDolar = precos.euroParaDolar * 10000
        dolarParaEuro = precos.dolarParaEuro * 10000

        query = """INSERT INTO precos (USD_BRL, BRL_USD, EUR_BRL, BRL_EUR, EUR_USD, USD_EUR) VALUES('%i','%i','%i','%i','%i','%i' )""" % (dolarParaReal,realParaDolar, euroParaReal, realParaEuro, euroParaDolar, dolarParaEuro)
        print( query)
            
        try:
            db.execute(query)
            con.commit()
            db.close()
            return{
                'status': 201,
                'message':'Valor criado com sucesso'
            }
        except:
            con.rollback()
            db.close()
            
            return {
                'status': 400,
                'message': "Erro ao tentar enviar um valor"
            }