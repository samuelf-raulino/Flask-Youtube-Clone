import sqlite3
import random

# conecta no banco
conn = sqlite3.connect("databases/videos.db")
cursor = conn.cursor()

# dados aleatórios
titulos = [
    "Nightwish - The Kinslayer [HD]"
]

descricoes = [
    "Premier montage réalisé par moi même à partir du Seigneur Des Anneaux"
]

thumbnails = [
    "https://i.ytimg.com/vi/Sp8ZTF20py4/hq720.jpg?sqp=-oaymwEnCNAFEJQDSFryq4qpAxkIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB&rs=AOn4CLA9Cyz2dgZHRzT6pECHGPqGb11mOQ"
]

urls = [
    "https://www.youtube.com/watch?v=Sp8ZTF20py4"
]

# escolhe aleatoriamente
titulo = random.choice(titulos)
descricao = random.choice(descricoes)
thumbnail = random.choice(thumbnails)
url = random.choice(urls)

# insere no banco
cursor.execute("""
INSERT INTO conteudos (thumbnail, titulo, descricao, url)
VALUES (?, ?, ?, ?)
""", (thumbnail, titulo, descricao, url))

conn.commit()
conn.close()

print("Vídeo aleatório inserido com sucesso!")
