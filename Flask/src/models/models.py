from main import app
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy(app)
class UsuarioModel(db.Model):
    __tablename__ ='usuarios'
    id=db.Column(db.Integer(),primary_key=True)
    nome=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    senha=db.Column(db.String(100),nullable=False)
    def __init__(self,nome,email,senha):
        self.nome=nome
        self.email=email
        self.senha=senha
