from flask import Blueprint, request, session, redirect, url_for, flash
from models.usuario import Usuario

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    usuario_db = Usuario.autenticar(usuario, senha)

    if not usuario_db:
        flash("Usuário ou senha inválidos.")
        return redirect(url_for("home.home"))

    session["usuario_id"] = usuario_db.cd_usuario
    session["usuario_login"] = usuario_db.login
    return redirect(url_for("home.menu"))

@auth_bp.route("/logout")
def logout():
    session.clear()

    return redirect(url_for("home.home"))