import mysql.connector
from api.model.db.private.secret import DB_host, DB_user, DB_password, DB_dbname

def conexao():
    con = mysql.connector.connect(host=DB_host, user=DB_user, password=DB_password, database=DB_dbname) 
    return con