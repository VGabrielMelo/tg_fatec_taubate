from flask import Flask
from flask_restx import Api
from src.variables.variables import variables

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        
        self.app.config['SQLALCHEMY_DATABASE_URI']=variables.db_uri
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
        self.app.config['SQLALCHEMY_ECHO']=True

        self.api = Api(
            self.app,
            version='1.0',
            title='API de processamento de linguagem natural',
            description='Api para o processamento de comentários de redes sociais e plataformas de emprego com a finalidade de analisar a reputação de uma empresa específica',
            doc='/docs'
        )
        
    
    def run(self):
        self.app.run(debug=True)
server = Server()