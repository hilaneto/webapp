from flask import Blueprint, request, redirect, url_for, session
from models.usuario import Usuario

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    login = request.form.get("usuario", "")
    senha = request.form.get("senha", "")

    usuario = Usuario.autenticar(login, senha)

    if usuario:
        session["usuario_id"] = usuario.cd_usuario
        session["usuario_login"] = usuario.login
        return redirect(url_for("home.menu"))

    return "Login não encontrado"

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.home"))