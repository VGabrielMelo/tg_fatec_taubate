from sqlalchemy import null
from src.exceptions.request_error import RequestError
from src.utils.jwt_util import jwt_util
from src.utils.indeed import getReviewsIndeed
from src.server.instance import server

nlp = server.nlp

class EmpresaService:
    
    def getEmpresaByName(self, nome_empresa):
        reviews_indeed = getReviewsIndeed(nome_empresa)

        try:
            dados_indeed = nlp.AnaliseSentimento(reviews_indeed['reviews'])
            total_indeed = dados_indeed['total']
            response_indeed = {
                'porcentagem_positivo':float(format(((dados_indeed['positivo']/total_indeed)*100),".2f")),
                'porcentagem_negativo':float(format(((dados_indeed['negativo']/total_indeed)*100),".2f")),
                'porcentagem_neutro':float(format(((dados_indeed['neutro']/total_indeed)*100),".2f"))
                #'top_positivos': dados_indeed['positivo'][slice(-10,len(processados_indeed['positivo']))],
                #'top_negativos': dados_indeed['negativo'][slice(-10,len(processados_indeed['negativo']))]
            }
            return response_indeed
        except Exception as e:
            print(e)
empresaService = EmpresaService()