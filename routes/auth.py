from flask import Blueprint, render_template, request, session, redirect, url_for
from models.usuario import Usuario

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/logar")
def logar():
    return render_template("login.html")


@auth_bp.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    usuario_db = Usuario.autenticar(usuario, senha)
    if not usuario_db:
        return render_template("login.html", mensagem="Usuário ou senha inválidos.")

    session["usuario_id"] = usuario_db.cd_usuario
    session["usuario_login"] = usuario_db.login
    return redirect(url_for("home.sistema"))


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home.home"))