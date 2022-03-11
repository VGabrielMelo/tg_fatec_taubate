from src.controllers.empresa import *
from src.controllers.usuario import *
from src.models.models import *

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://rnsibxkn:glTdKMCJR9PMpTrmlEtrpMJW2StbFzBc@tuffi.db.elephantsql.com/rnsibxkn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=True

api = Api(
    app,
    version='1.0',
    title='API de processamento de linguagem natural',
    description='Api para o processamento de comentários de redes sociais e plataformas de emprego com a finalidade de analisar a reputação de uma empresa específica',
    doc='/docs'
)

if __name__=='__main__':
    db.create_all()
    app.run(debug=True)

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