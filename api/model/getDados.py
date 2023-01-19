from api.model.db.conexao import conexao

def MD_getNow():
    con = conexao()
    cur = con.cursor()
    cur.execute("SELECT * FROM precos ORDER BY id DESC LIMIT 1")
    response = cur.fetchall()
    cur.close()
    con.commit()
    con.close()
    return response

def MD_getDay():
    con = conexao()
    cur = con.cursor()
    cur.execute("SELECT * FROM day ORDER BY id DESC LIMIT 24")
    response = cur.fetchall()
    cur.close()
    con.commit()
    con.close()
    return response