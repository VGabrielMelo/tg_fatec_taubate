from src.exceptions.request_error import RequestError
class AuthUtil:
    def isLogged(self, auth_header):
        if(auth_header):
            return auth_header.split(" ")[1] 
        else:
            raise RequestError("Token inválido.", 401) 
auth_util = AuthUtil()