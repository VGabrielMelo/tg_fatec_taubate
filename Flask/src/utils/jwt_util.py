import jwt
import datetime
from src.variables.variables import variables
from src.exceptions.request_error import RequestError

jwt_secret = variables.jwt_secret
algorithm = "HS256"

class JwtUtil:

    def create_token(self, id,agora):
        exp = datetime.timedelta(hours=3)
        obj_token = {"exp": agora+exp,"iat": agora,"id":id}
        return jwt.encode(obj_token,jwt_secret,algorithm=algorithm)

    def decode_token(self, token):
        try:
            return jwt.decode(token,jwt_secret,algorithms=algorithm)
        except Exception as err:
            raise RequestError("Token inválido.", 401)
jwt_util = JwtUtil()