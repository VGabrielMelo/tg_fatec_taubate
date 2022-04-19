from src.exceptions.request_error import RequestError
from src.utils.jwt_util import jwt_util
from src.utils.twitter import searchReviewsTwitter
from src.utils.glassdoor import getReviewsGlassdoor
import asyncio

class EmpresaService:
    def getEmpresaByName(self, nome_empresa):
        #reviews_glassdoor = getReviewsGlassdoor(nome_empresa)
        reviews_twitter = searchReviewsTwitter(nome_empresa)
        
        """ reviews_twitter,reviews_glassdoor = await asyncio.gather(
            getReviewsGlassdoor(nome_empresa),
            getReviewsTwitter(nome_empresa)
        ) """
        return reviews_twitter

empresaService = EmpresaService()