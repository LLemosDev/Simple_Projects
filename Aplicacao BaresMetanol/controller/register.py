from flask import Blueprint, request , redirect, url_for, render_template
from models.db import db
from models.agenda import agenda
from utils.cripto import encrypt

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        tel = request.form.get("telefone")
        endereco = request.form.get("endereco")
        reputacao = request.form.get("estrelas")
        status = request.form.get("status")

        aberto = True if(status == "1") else False

        cypher_tel = encrypt(tel)
        cypher_endereco = encrypt(endereco)

        novo_bar = agenda(
            nome=nome,
            email=email,
            telefone=cypher_tel,
            endereco=cypher_endereco,
            estrelas=reputacao,
            aberto = aberto
        )

        db.session.add(novo_bar)
        db.session.commit()

        return redirect(url_for("home.home"))
    
    return render_template("register.html")