from flask import Flask, url_for,render_template,Blueprint  


home_route = Blueprint('home',__name__)

@home_route.route('/')
def home():
    titulo = "teste de titulo"
    texto = 1
    image = "background.jpg"
    return render_template('index.html',titulo=titulo,texto=texto,image=image)