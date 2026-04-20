def get_conteudos(id=0):
    if id==0:
        import sqlite3 

        conn = sqlite3.connect("databases/videos.db")

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM conteudos")
        conteudos = cursor.fetchall()

        cursor.close()
        conn.close()
        return conteudos
    else:
        import sqlite3 

        conn = sqlite3.connect("databases/videos.db")

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM conteudos WHERE id = ?",(id,))
        conteudo = cursor.fetchall()

        cursor.close()
        conn.close()
        return conteudo
def add_conteudo(thumbnail,titulo,descricao,url,user):
    import sqlite3 
    conn = sqlite3.connect("databases/videos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO conteudos (thumbnail,titulo,descricao,url,user) VALUES (?,?,?,?,?)",(thumbnail,titulo,descricao,url,user))
    conn.commit()
    print("valor adicionado!")
    cursor.execute("SELECT id FROM conteudos WHERE url = ?",(url,))
    id = cursor.fetchall()
    cursor.close()
    conn.close()
    return id