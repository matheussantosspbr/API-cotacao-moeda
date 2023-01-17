import mysql.connector
from api.model.db.private.secret import host, user, password, dbname

def conexao():
    con = mysql.connector.connect(host=host, user=user, password=password, database=dbname) 
    return con