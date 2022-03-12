from src.server.instance import server
from src.server.controllers.empresa import *
from src.server.controllers.usuario import *
from src.models.models import db
db.create_all()
server.run()

""" from flask import Flask
import urllib.request

import json
import sys

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Pesquisa")
def pesquisa():
    #Aqui vai as APIs dos sites
    try:
        retornoL = []
        retorno = json.dumps([e.toJSON() for e in retornoL])
    except:
        print ("error ", sys.exc_info()[0])
    return retorno

@app.route("/Analise_Sentimentos")
def analise_sentimentos():
    #Aqui vai a execução das anaálises com o fast.ia
    try:
        retornoL = []
        retorno = json.dumps([e.toJSON() for e in retornoL])
    except:
        print ("error ", sys.exc_info()[0])
    return retorno

@app.route ("/Contagem_Palavras")
def contagem_palavras():
    #Realiza as contagens das palavras e retorna a palavra seguida da quantidade em um int
    try:
        retornoL = []
        retorno = json.dumps([e.toJSON() for e in retornoL])
    except:
        print ("error ", sys.exc_info()[0])
    return retorno
    
@app.route("/Criacao_Relatorio")
def criacao_relatorio():
    #Criação de um relatório com os dados obtidos das respostas da análise.
    try:
        retornoL = []
        retorno = json.dumps([e.toJSON() for e in retornoL])
    except:
        print ("error ", sys.exc_info()[0])
    return retorno """