from .db import db

class agenda(db.Model):
    __tablename__ = 'agenda'

    codigo = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(255), nullable=False)
    endereco = db.Column(db.String(255), nullable=False)
    estrelas = db.Column(db.Integer, nullable = False)
    aberto =  db.Column(db.Boolean, default=False)