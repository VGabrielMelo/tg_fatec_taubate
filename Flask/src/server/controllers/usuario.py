from http import server
from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server

app, api = server.app, server.api
base_endpoint="/usuarios"


class UsuarioController(Resource):

    @app.route(f'/{base_endpoint}/', methods=['POST'])
    def create():
        usuario = api.payload
        return usuario,201

