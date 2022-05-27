from sqlalchemy import null
from src.exceptions.request_error import RequestError
from src.utils.jwt_util import jwt_util
from src.utils.twitter import searchReviewsTwitter
from src.utils.glassdoor import getReviewsGlassdoor
from src.utils.indeed import getReviewsIndeed
from src.server.instance import server

nlp = server.nlp

class EmpresaService:
    
    def getEmpresaByName(self, nome_empresa):
        #reviews_glassdoor = getReviewsGlassdoor(nome_empresa)
        #reviews_twitter = searchReviewsTwitter(nome_empresa)
        reviews_indeed = getReviewsIndeed(nome_empresa)

        try:
            def ordenar(e):
                return e[0]

            dados_indeed = nlp.AnaliseSentimento(reviews_indeed['reviews'])
            processados_indeed = {
                'positivo':[],
                'negativo':[],
                'neutro':[]
            }
            for d in dados_indeed:
                if(d[0]=="Positivo"):
                    processados_indeed['positivo'].append([d[1],reviews_indeed['reviews'][d[2]]['title']])
                if(d[0]=="Negativo"):
                    processados_indeed['negativo'].append([d[1],reviews_indeed['reviews'][d[2]]['title']])
                if(d[0]=="Neutro"):
                    processados_indeed['neutro'].append([d[1],reviews_indeed['reviews'][d[2]]['title']])
            processados_indeed['positivo'].sort(key=ordenar)
            processados_indeed['negativo'].sort(key=ordenar)
            processados_indeed['neutro'].sort(key=ordenar)
            response_indeed = {
                'porcentagem_positivo':float(format(((len(processados_indeed['positivo'])/len(reviews_indeed['reviews']))*100),".2f")),
                'porcentagem_negativo':float(format(((len(processados_indeed['negativo'])/len(reviews_indeed['reviews']))*100),".2f")),
                'porcentagem_neutro':float(format(((len(processados_indeed['neutro'])/len(reviews_indeed['reviews']))*100),".2f")),
                'top_positivos': processados_indeed['positivo'][slice(-10,len(processados_indeed['positivo']))],
                'top_negativos': processados_indeed['negativo'][slice(-10,len(processados_indeed['negativo']))]
            }
            return response_indeed
        except Exception as e:
            print(e)

empresaService = EmpresaService()