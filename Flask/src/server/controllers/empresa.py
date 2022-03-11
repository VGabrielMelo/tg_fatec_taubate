from http import server
from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api
base_endpoint="/empresas"


class EmpresaController(Resource):

    @app.route(f'/{base_endpoint}/<string:nome_empresa>/',  methods=['GET'])
    def get(nome_empresa):
        return nome_empresa,200

