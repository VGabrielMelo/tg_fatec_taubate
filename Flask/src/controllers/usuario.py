from flask import Flask, jsonify, make_response, request
from flask_restx import Api, Resource
from src.exceptions.request_error import RequestError

from src.models.docModels import cadastroModel, loginModel
from src.server.instance import server
from src.services.usuario import usuarioService

app, api = server.app, server.api
ns = api.namespace('usuarios', description='API de usuário')

@ns.route('/',methods=['POST','GET'])
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
    def get(self):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if(auth_token):
            try:
                user = usuarioService.getUsuario(auth_token)
                usuario = {'nome':user.nome,'email':user.email}
                print(usuario)
                return make_response(jsonify({'message':'Usuário encontrado.','user':usuario}), 200)
            except RequestError as err:
                return make_response(jsonify({'message':err.message}), err.status_code)
            except Exception:
                return make_response(jsonify({'message':'Não foi possível encontrar o usuário.'}), 400)
        else:
            return make_response(jsonify({'message':'Token inválido.'}), 401)

@ns.route('/auth',methods=['POST'])
class UsuarioAuth(Resource):
    
    @ns.expect(loginModel)
    @api.doc(responses={
        201: 'Login realizado com sucesso.',
        400: 'Não foi possível realizar o login.',
        401: 'Não foi possível realizar login. Número de tentativas excedidas, aguarde 5 minutos e tente novamente.',
        401: 'Não foi possível realizar login. Login ou senha incorretos.'
    })
    def post(self):
        usuario = api.payload
        try:
            token = usuarioService.login(usuario['email'],usuario['senha'])
            return make_response(jsonify({'message':'Login realizado com sucesso.','token':token}), 200)
        except RequestError as err:
            return make_response(jsonify({'message':err.message}), err.status_code)
        except Exception as err:
            return make_response(jsonify({'message':'Não foi possível realizar login.'}), 400)
    
 

        
