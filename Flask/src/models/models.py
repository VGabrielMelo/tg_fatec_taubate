from src.server.instance import server
from flask_sqlalchemy import SQLAlchemy

app = server.app

db=SQLAlchemy(app)

class UsuarioModel(db.Model):
    __tablename__ ='usuarios'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    nome=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    senha=db.Column(db.String(100),nullable=False)
    def __init__(self,nome,email,senha):
        self.nome=nome
        self.email=email
        self.senha=senha
class LoginModel(db.Model):
    __tablename__ ='login'
    id=db.Column(db.Integer(),primary_key=True,autoincrement=True)
    data=db.Column(db.DateTime(),nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    #usuario=db.relationship('UsuarioModel',backref='login')
    can_login=db.Column(db.Boolean(),nullable=False)
    def __init__(self,data,usuario_id,can_login):
        self.data=data
        self.usuario_id=usuario_id
        self.canLogin=can_login