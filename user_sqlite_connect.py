def add_user(user,email,senha):
    import sqlite3 
    conn = sqlite3.connect("databases/usuarios.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (user,email,senha) VALUES (?,?,?)",(user,email,senha))
    conn.commit()
    print("Usuario adicionado!")
    cursor.close()
    conn.close()
def ver_user(user,senha):
    import sqlite3 
    conn = sqlite3.connect("databases/usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    ver = False
    for x in usuarios:
        if x[1] == user and x[3] == senha:
            ver = True
    return ver
def get_id(user,senha):
    import sqlite3 
    conn = sqlite3.connect("databases/usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE user = ? AND senha = ?",(user,senha))
    id = cursor.fetchall()
    cursor.close()
    conn.close()
    return id
def get_dates(id=0,user=""):
    if id == 0 and user!="": 
        import sqlite3 
        conn = sqlite3.connect("databases/usuarios.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE user = ?",(user,))
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado
    if id != 0 and user=="": 
        import sqlite3 
        conn = sqlite3.connect("databases/usuarios.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = ?",(id,))
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado