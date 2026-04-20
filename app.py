from flask import Flask,redirect,url_for,render_template,request,flash,session
from video_sqlite_connect import get_conteudos,add_conteudo
from user_sqlite_connect import add_user,ver_user,get_id,get_dates
from extra_funcs import youtube_embed
app = Flask(__name__)
app.secret_key = "secret key"

@app.route("/")
def main():
    return redirect(url_for("cadastro"))
@app.route("/home")
def home():
    conteudos = get_conteudos()
    return render_template("home.html",conteudos=conteudos,user = get_dates(session["user"])[0][1])
@app.route("/logout")
def logout():
    session["user"] = 0
    return redirect(url_for("home"))
@app.route("/video/<int:id>")
def video(id):
    conteudo = get_conteudos(id)[0]
    link = youtube_embed(conteudo[4])
    return render_template("video.html",conteudo=conteudo,link=link)
@app.route("/addVideo",methods=["POST","GET"])
def addVideo():
    if request.method == "POST":
        thumbnail = request.form["thumbnail"]
        titulo = request.form["titulo"]
        descrição = request.form["descricao"]
        url = request.form["url"]
        id = add_conteudo(thumbnail,titulo,descrição,url,get_dates(session["user"])[0][1])
        return redirect(url_for("video",id=id[0][0]))
    return render_template("addVideo.html")
@app.route("/cadastro",methods=["GET","POST"])
def cadastro():
    if request.method=="POST":
        user = request.form["user"]
        email = request.form["email"]
        senha = request.form["senha"]
        add_user(user,email,senha)
        return redirect(url_for("login"))
    return render_template("cadastro.html")
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form["user"]
        senha = request.form["senha"]
        ver = ver_user(user,senha)
        if ver == True:
            session["user"] = get_id(user,senha)[0][0]
            return redirect(url_for("home"))
        else:
            flash("senha incorreta")
            return redirect(url_for("login"))
    return render_template("login.html")
@app.route("/channel/<string:user>")
def channel(user):
    permissao = False
    if user == get_dates(session["user"])[0][1]:
        permissao = True
    dates = get_dates(user=user)
    return render_template("channel.html",permissao=permissao,user=user,dates=dates)

app.run(debug=True)