from flask import Flask, jsonify, make_response
from flask_restx import Api, Resource

from src.models.docModels import cadastroModel, loginModel
from src.server.instance import server
from src.services.usuario import usuarioService

app, api = server.app, server.api
ns = api.namespace('usuarios', description='API de usuário')

@ns.route('/',methods=['POST','GET','PUT','PATCH','DELETE'])
class Usuario(Resource):
    @ns.expect(cadastroModel)
    @api.doc(responses={
        201: 'Cadastro realizado com sucesso',
        400: 'Não foi possível realizar o cadastro'
    })
    def post(self):
        usuario = api.payload
        try:
            usuarioService.cadastro(usuario['nome'],usuario['email'],usuario['senha'])
            return make_response(jsonify({'message':'Cadastro realizado com sucesso.'}), 201)
        except Exception:
            return make_response(jsonify({'message':'Não foi possível realizar o cadastro.'}), 400)

@ns.route('/auth',methods=['POST'])
class UsuarioAuth(Resource):
    @ns.expect(loginModel)
    def post(self):
        usuario = api.payload
        try:
            token = usuarioService.login(usuario['email'],usuario['senha'])
            return make_response(jsonify({'message':'Login realizado com sucesso.','token':token}), 200)
        except Exception:
            return make_response(jsonify({'message':'Não foi possível realizar o login.'}), 401)

        
