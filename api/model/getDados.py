from api.model.db.conexao import conexao

def MD_getMinuto():
    con = conexao()
    cur = con.cursor()
    cur.execute("SELECT * FROM precos ORDER BY id DESC LIMIT 1")
    response = cur.fetchall()
    cur.close()
    con.commit()
    con.close()
    return response