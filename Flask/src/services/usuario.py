import jwt
import datetime
from flask_bcrypt import Bcrypt

from src.server.instance import server
from src.variables.variables import variables
from src.exceptions.request_error import RequestError
from src.models.models import UsuarioModel,LoginModel,db

app = server.app
bcrypt = Bcrypt(app)
jwt_secret = variables.jwt_secret


class UsuarioService:

    def cadastro(self, nome,email,senha):
            pw_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
            user = UsuarioModel(nome,email,pw_hash)
            db.session.add(user)
            db.session.commit()

    def login(self, email,senha):
        user = UsuarioModel.query.filter_by(email=email).first()
        agora = datetime.datetime.now(tz=datetime.timezone.utc)
        exp = datetime.timedelta(hours=3)
        logins = LoginModel.query.order_by(LoginModel.data.desc()).filter_by(usuario_id=user.id, can_login=False).limit(3)
        if(logins.count()==3):
            first_login = datetime.datetime.replace(logins[2].data)
            last_login = datetime.datetime.replace(logins[0].data)
            time_diference = (last_login-first_login).total_seconds()/60
            time_diference = int(time_diference * (10**0))/(10**0)
            if(time_diference<5):
                raise RequestError('Não foi possível realizar login. Número de tentativas excedidas, aguarde 5 minutos e tente novamente.', status_code=401)
        if(bcrypt.check_password_hash(user.senha, senha)):
            login = LoginModel(agora,user.id,True)
            obj_token = {"exp": agora+exp,"iat": agora,"id":user.id}
            token = jwt.encode(obj_token,jwt_secret,algorithm="HS256")
            db.session.add(login)
            db.session.commit()
            return token
        else:
            if(user is not None):
                login = LoginModel(agora,user.id,False)
                db.session.add(login)
                db.session.commit()
            raise RequestError('Não foi possível realizar login. Login ou senha incorretos.', status_code=401)    
            
    def getUsuario(self, encoded):
        try:
            token=jwt.decode(encoded,jwt_secret,algorithms="HS256")
            user = UsuarioModel.query.filter_by(id=token['id']).first()
            if(user is not None):
                return user
            else:
                raise RequestError('Usuário não encontrado.', status_code=404)       
        except Exception as e:
            raise RequestError('Token inválido.', status_code=401)       


usuarioService = UsuarioService()