from flask import Flask, jsonify, make_response, request
from flask_restx import Api, Resource

from src.exceptions.request_error import RequestError
from src.models.docModels import cadastroModel, loginModel
from src.server.instance import server
from src.services.usuario import usuarioService
from src.utils.auth_util import auth_util

app, api = server.app, server.api
ns = api.namespace('usuarios', description='API de usuário')

@ns.route('/',methods=['POST','GET','DELETE','PATCH'])
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


    @api.doc(responses={
        200: 'Usuário encontrado.',
        400: 'Não foi possível encontrar o usuário.',
        401: 'Token inválido.',
        404: 'Usuário não encontrado.'
    })
    def get(self):
        try:
            auth_token = auth_util.isLogged(request.headers.get('Authorization'))
            user = usuarioService.getUsuarioById(auth_token)
            usuario = {'nome':user.nome,'email':user.email}
            return make_response(jsonify({'message':'Usuário encontrado.','user':usuario}), 200)
        except RequestError as err:
            return make_response(jsonify({'message':err.message}), err.status_code)
        except Exception:
                return make_response(jsonify({'message':'Não foi possível encontrar o usuário.'}), 400)


    @api.doc(responses={
        204: 'Usuário deletado com sucesso.',
        400: 'Não foi possível encontrar o usuário.',
        401: 'Token inválido.',
        404: 'Usuário não encontrado.'
    })
    def delete(self):
        try:
            auth_token = auth_util.isLogged(request.headers.get('Authorization'))
            usuarioService.deleteUsuario(auth_token)
            return make_response(jsonify({'message':'Usuário deletado com sucesso.'}), 204)
        except RequestError as err:
            return make_response(jsonify({'message':err.message}), err.status_code)
        except Exception:
            return make_response(jsonify({'message':'Não foi possível encontrar o usuário.'}), 400)

    @ns.expect(cadastroModel)
    @api.doc(responses={
        200: 'Usuário atualizado com sucesso.',
        400: 'Não foi possível atualizar o usuário.',
        401: 'Token inválido.',
        404: 'Usuário não encontrado.'
    })
    def patch(self):
        try:
            auth_token = auth_util.isLogged(request.headers.get('Authorization'))
            usuarioService.updateUsuario(auth_token,api.payload)
            return make_response(jsonify({'message':'Usuário atualizado com sucesso.'}), 200)
        except RequestError as err:
            return make_response(jsonify({'message':err.message}), err.status_code)
        except Exception as err:
            print (err)
            return make_response(jsonify({'message':'Não foi possível atualizar o usuário.'}), 400)


@ns.route('/auth',methods=['POST'])
class UsuarioAuth(Resource):
    
    @ns.expect(loginModel)
    @api.doc(responses={
        201: 'Login realizado com sucesso.',
        400: 'Não foi possível realizar o login.',
        401: 'Não foi possível realizar login. Número de tentativas excedidas, aguarde 5 minutos e tente novamente.',
        401: 'Não foi possível realizar login. Login ou senha incorretos.',
        404: 'Usuário não encontrado.'

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
    
 

        
