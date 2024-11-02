from flask import Flask, url_for,render_template,Blueprint,request,Response
from modelo import DB 

db = DB()

missions_route = Blueprint('Missions',__name__)
 
@missions_route.route('/',methods=["GET"])
def home():
    missions = db.View()
    print(type(missions))
    # for row in clientes:
    #     print(row)
    return render_template('Missions.html',data=missions)
    
@missions_route.route('/new-mission',methods=["GET"])
def new_mission():

    return render_template('Criar-Missao.html')

@missions_route.route('/new-mission/inserir',methods=["POST"])
def insert_client():
    form_data = request.get_json()
    # print("Dados recebidos:", form_data["Nome"],form_data["Lancamento"],form_data["Destino"],form_data["Estado"],form_data["Tripulacao"],form_data["Cargas"],form_data["Custo"],form_data["Duracao"],form_data["Status"],form_data["Nave"])
    
    # Nome,Lancamento,Destino,Estado,Tripulacao,Cargas,Custo,Duracao,Status,Nave
    
    if(db.inserir(form_data["Nome"],form_data["Lancamento"],form_data["Destino"],form_data["Estado"],form_data["Tripulacao"],form_data["Cargas"],form_data["Custo"],form_data["Duracao"],form_data["Status"],form_data["Nave"],)) == True:
        resp = Response("Missão inserido com sucesso!")
    else:
        resp = Response("Erro na inserção")
  
    return resp

@missions_route.route('/deletar',methods=["DELETE"])
def deletarMissao():
     form_data = request.get_json()
     db.delete(form_data["id"])
     resp = Response("Missão deletada com sucesso!")
     return resp
     
@missions_route.route('/att',methods=["GET"])
def att(): 
    if 'id' in request.args:
    # parameter 'varname' is specified
        id = request.args.get('id')
    else:
        return "Conexão não pode ser realizada"
    
    if(db.View(id) != None):
        missions = db.View(id)
    else:
        return "Indice não encontrado"

    # Nome,Lancamento,Destino,Estado,Tripulacao,Cargas,Custo,Duracao,Status,Nave

    # print(type(missions))
    # print(id) 
    tripulantes = missions[5].split(',')
    Cargas = missions[6].split(',')
    return render_template('att.html',id=missions[0],nome=missions[1],Lancamento=missions[2],Destino=missions[3],Estado=missions[4],Tripulacao=tripulantes,Cargas=Cargas,Custo=missions[7],Duracao=missions[8],Status=missions[9],Nave=missions[10])

@missions_route.route('/att/submit',methods=["PUT"])
def submit():
    form_data = request.get_json()
    if(db.update(form_data["id"],form_data["Nome"],form_data["Lancamento"],form_data["Destino"],form_data["Estado"],form_data["Tripulacao"],form_data["Cargas"],form_data["Custo"],form_data["Duracao"],form_data["Status"],form_data["Nave"],))  == True: 
        resp = Response("Missão inserido com sucesso!")
    else:
        resp = Response("Erro na inserção")
  
    return resp    
