from src.exceptions.request_error import RequestError
from src.utils.jwt_util import jwt_util
from src.utils.twitter import searchReviewsTwitter
from src.utils.glassdoor import getReviewsGlassdoor
from src.utils.indeed import getReviewsIndeed

import asyncio

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
        #função_de_analise(reviews_twitter,reviews_glassdoor)
        return reviews_indeed

empresaService = EmpresaService()