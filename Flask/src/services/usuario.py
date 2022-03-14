from flask_bcrypt import Bcrypt
from src.models.models import UsuarioModel,LoginModel, db
from src.server.instance import server
import datetime
from src.variables.variables import variables
import jwt
from src.error_handlers.error_handlers import handle_bad_request, handle_unauthorized
app = server.app
jwt_secret = variables.jwt_secret
bcrypt = Bcrypt(app)

class UsuarioService:
    def cadastro(self, nome,email,senha):
            pw_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
            #bcrypt.check_password_hash(pw_hash, 'hunter2') checa se a senha coincide com o hash
            user = UsuarioModel(nome,email,pw_hash)
            db.session.add(user)
            db.session.commit()
    def login(self, email,senha):
            try:
                user = UsuarioModel.query.filter_by(email=email).first()
                agora = datetime.datetime.now(tz=datetime.timezone.utc)
                exp = datetime.timedelta(hours=3)
                logins = LoginModel.query.order_by(LoginModel.data.desc()).filter_by(usuario_id=user.id).limit(3)
                if(logins.count()==3):
                    first_login = datetime.datetime.replace(logins[2].data)
                    last_login = datetime.datetime.replace(logins[0].data)
                    time_diference = (last_login-first_login).total_seconds()/60
                    time_diference = int(time_diference * (10**0))/(10**0)
                    if(time_diference<5):
                        handle_unauthorized("Não foi possível realizar login. Número de tentativas excedidas, aguarde 5 minutos e tente novamente.")
                if(bcrypt.check_password_hash(user.senha, senha)):
                    login = LoginModel(agora,user.id,True)
                    token = jwt.encode(
                        {"exp": agora+exp,"iat": agora},
                        jwt_secret,
                        algorithm="HS256"
                    )
                    db.session.add(login)
                    db.session.commit()
                    return token
                else:
                    if(user is not None):
                        login = LoginModel(agora,user.id,False)
                        db.session.add(login)
                        db.session.commit()
                        handle_unauthorized("Não foi possível realizar login. Senha ou login incorretos.")
            except Exception as err:
                print(err)
                
usuarioService = UsuarioService()