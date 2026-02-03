from flask import Flask, render_template, Blueprint
from models.db import db
from models.agenda import agenda
from utils.cripto import decrypt

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    lista_bares = agenda.query.all()
    bares = []

    for bar in lista_bares:
        obj_temp = {"nome": bar.nome, "email": bar.email, "telefone": decrypt(bar.telefone),
                    "endereco": decrypt(bar.endereco), "estrelas": bar.estrelas, "aberto": bar.aberto}
        
        if bar.estrelas > 4:
            obj_temp["mensagem"] = "Boa"
        elif bar.estrelas > 3:
            obj_temp["mensagem"] = "Mediana"
        else:
            obj_temp["mensagem"] = "Baixa"
        
        bares.append(obj_temp)

    return render_template("home.html", bares=bares)