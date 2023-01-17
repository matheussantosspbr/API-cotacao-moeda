from datetime import datetime
from api.model.key.token import secret_token, public_token
from api.model.db.conexao import conexao

def indexPost(data):
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
        
        query = """INSERT INTO precos
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
    else:
        return {
           'status': 503,
           'message': 'Token inválido'
        }
