""" from src.server.instance import server
from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

ns = api.namespace('empresas', description='API de empresa')

@ns.route('/<string:nome_empresa>/')
class Empresa(Resource):
    @api.doc(params={'nome_empresa': 'Nome da empresa que vai ser realizada a pesquisa'})
    def get(self, nome_empresa):
        return nome_empresa,200 

 """