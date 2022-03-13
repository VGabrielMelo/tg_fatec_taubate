from flask import Flask, jsonify, make_response
from flask_restx import Api, Resource, fields
from flask_bcrypt import Bcrypt

from src.models.models import UsuarioModel, db
from src.server.instance import server

app, api = server.app, server.api

ns = api.namespace('usuarios', description='API de usuário')

bcrypt = Bcrypt(app)

usuarioModel = api.model('Usuario', {
    'nome': fields.String(required=True, description='O nome do usuário'),
    'email': fields.String(required=True, description='O email do usuário'),
    'senha': fields.String(required=True, description='A senha do usuário'),
})

@ns.route('/',methods=['POST','GET','PUT','PATCH','DELETE'])
class Usuario(Resource):

    @ns.expect(usuarioModel)
    #@ns.marshal_with(usuarioModel)
    #@ns.doc("Cadastra um novo usuário")
    def post(self):
        usuario = api.payload
        try:
            pw_hash = bcrypt.generate_password_hash(usuario['senha']).decode('utf-8')
            #bcrypt.check_password_hash(pw_hash, 'hunter2') checa se a senha coincide com o hash
            user = UsuarioModel(usuario['nome'],usuario['email'],pw_hash)
            db.session.add(user)
            db.session.commit()
            return make_response(jsonify({'message':'Cadastro realizado com sucesso.'}), 201)
        except:
            return make_response(jsonify({'message':'Não foi possível realizar o cadastro.'}), 400)

        
