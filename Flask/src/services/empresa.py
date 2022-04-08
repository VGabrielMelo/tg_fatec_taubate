
from src.exceptions.request_error import RequestError
from src.utils.jwt_util import jwt_util
from src.utils.tweeter import search
from src.utils.glassdoor import getReviews


class EmpresaService:


    def getEmpresaByName(self, nome_empresa):
        return getReviews(nome_empresa)

empresaService = EmpresaService()