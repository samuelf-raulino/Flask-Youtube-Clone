import sqlite3
import random

# conecta no banco
conn = sqlite3.connect("databases/videos.db")
cursor = conn.cursor()

# dados aleatórios
titulos = [
    "Vídeo incrível",
    "Conteúdo aleatório",
    "Aprenda algo novo",
    "Curiosidades da internet",
    "Vídeo recomendado"
]

descricoes = [
    "Um vídeo muito interessante.",
    "Conteúdo escolhido aleatoriamente.",
    "Você vai gostar desse vídeo.",
    "Assista até o final.",
    "Vale a pena conferir."
]

thumbnails = [
    "thumb1.jpg",
    "thumb2.jpg",
    "thumb3.jpg"
]

urls = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://www.youtube.com/watch?v=9bZkp7q19f0",
    "https://www.youtube.com/watch?v=l482T0yNkeo"
]

# escolhe aleatoriamente
titulo = random.choice(titulos)
descricao = random.choice(descricoes)
thumbnail = random.choice(thumbnails)
url = random.choice(urls)

# insere no banco
cursor.execute("""
DELETE FROM conteudos WHERE id = ?
""", (1, ))

conn.commit()
conn.close()

print("Vídeo aleatório deletado com sucesso!")
