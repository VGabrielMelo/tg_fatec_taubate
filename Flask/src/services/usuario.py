import datetime
from flask_bcrypt import Bcrypt

from src.server.instance import server
from src.exceptions.request_error import RequestError
from src.models.models import UsuarioModel,LoginModel,db
from src.utils.jwt_util import jwt_util

app = server.app
bcrypt = Bcrypt(app)

class UsuarioService:

    def cadastro(self, nome,email,senha):
            pw_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
            user = UsuarioModel(nome,email,pw_hash)
            db.session.add(user)
            db.session.commit()

    def login(self, email,senha):
        user = UsuarioModel.query.filter_by(email=email).first()
        agora = datetime.datetime.now(tz=datetime.timezone.utc)
        logins = LoginModel.query.order_by(LoginModel.data.desc()).filter_by(usuario_id=user.id, can_login=False).limit(3)
        if(logins.count()==3):
            first_login = datetime.datetime.replace(logins[2].data)
            last_login = datetime.datetime.replace(logins[0].data)
            time_diference = (last_login-first_login).total_seconds()/60
            time_diference = int(time_diference * (10**0))/(10**0)
            if(time_diference<5):
                raise RequestError('Não foi possível realizar login. Número de tentativas excedidas, aguarde 5 minutos e tente novamente.', status_code=401)
        if(bcrypt.check_password_hash(user.senha, senha)):
            token = jwt_util.create_token(user.id,agora)
            login = LoginModel(agora,user.id,True)
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
        token=jwt_util.decode_token(encoded)
        user = UsuarioModel.query.filter_by(id=token['id']).first()
        if(user is not None):
            return user
        else:
            raise RequestError('Usuário não encontrado.', status_code=404)       
  
    def deleteUsuario(self, encoded):
        user = self.getUsuario(encoded)
        db.session.delete(user)
        db.session.commit()

     


usuarioService = UsuarioService()