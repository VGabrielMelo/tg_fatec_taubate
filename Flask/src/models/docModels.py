from src.server.instance import server
from flask_restx import fields

app, api = server.app, server.api

cadastroModel = api.model('Usuario', {
    'nome': fields.String(required=True, description='O nome do usuário'),
    'email': fields.String(required=True, description='O email do usuário'),
    'senha': fields.String(required=True, description='A senha do usuário'),
})

loginModel = api.model('Login', {
    'email': fields.String(required=True, description='O email do usuário'),
    'senha': fields.String(required=True, description='A senha do usuário'),
})