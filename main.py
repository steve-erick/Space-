from flask import Flask, url_for,render_template   
from routes.home import home_route 
from routes.misions import missions_route
from flask_cors import CORS
#inicializando
app = Flask(__name__)   
CORS(app)
app.register_blueprint(home_route)
app.register_blueprint(missions_route, url_prefix='/Mission')

# @app.route('/', methods=['GET','POST','PUT'])
# def main():
#     titulo = "teste de titulo"
#     texto = "teste de texto"
#     return render_template('index.html',titulo=titulo,texto=texto)


# @app.route('/teste', methods=['GET','POST','PUT'])
# def rout():
#     return f"<a href='{url_for('main')}'>teste</a>"  
# 
#  
#debug
app.run(debug=True)