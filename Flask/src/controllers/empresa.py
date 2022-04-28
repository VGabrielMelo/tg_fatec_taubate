from flask import Flask, jsonify, make_response, request
from flask_restx import Api, Resource
from flask_cors import CORS
from src.utils.auth_util import AuthUtil
from src.exceptions.request_error import RequestError
from src.server.instance import server
from src.services.empresa import empresaService

app, api = server.app, server.api
ns = api.namespace('empresas', description='API de empresa')
CORS(app)
@ns.route('/<string:nome_empresa>/')
class Empresa(Resource):
    
    @api.doc(params={'nome_empresa': 'Nome da empresa'})
    @api.doc(responses={
        200: 'Empresa encontrada com sucesso.',
        400: 'Erro ao procurar empresa.',
        401: 'Token inválido.',
        404: 'Empresa não encontrada.'
    })
    def get(self, nome_empresa):
        try:
            empresa = empresaService.getEmpresaByName(nome_empresa)
            return make_response(jsonify(empresa), 200)
        except RequestError as err:
            return make_response(jsonify({'message':err.message}), err.status_code)
        except Exception as err:
            print (err)
            return make_response(jsonify({'message':''}), 400)

