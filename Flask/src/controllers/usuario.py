from flask import Flask, jsonify
from flask_restx import Api, Resource, fields

from src.server.instance import server

app, api = server.app, server.api

ns = api.namespace('usuarios', description='API de usuário')

usuarioModel = api.model('Usuario', {
    'nome': fields.String(required=True, description='O nome do usuário'),
    'email': fields.String(required=True, description='O email do usuário'),
    'senha': fields.String(required=True, description='A senha do usuário'),
})

@ns.route('/',methods=['POST','GET','PUT','PATCH','DELETE'])
class Usuario(Resource):

    @ns.expect(usuarioModel)
    @ns.marshal_with(usuarioModel)
    def post(self):
        usuario = api.payload
        return usuario,201
