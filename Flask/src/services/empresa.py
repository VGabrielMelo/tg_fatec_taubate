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

        """ IGNORAR, APENAS TESTANDO FUNÇÃO ASSINCRONA 
        reviews_twitter,reviews_glassdoor = await asyncio.gather(
            getReviewsGlassdoor(nome_empresa),
            getReviewsTwitter(nome_empresa)
        ) """
        try:
            return nlp.AnaliseSentimento(reviews_indeed['reviews'])
        except Exception as e:
            print(e)
        #return reviews_indeed['reviews']

empresaService = EmpresaService()