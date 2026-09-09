from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from suporte.upload import Upload

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload")
def upload():
    if "usuario_id" not in session:
        return redirect(url_for("home.home"))
    return render_template("upload.html")

@upload_bp.route("/upload/enviar", methods=["POST"])
def enviar():
    if "usuario_id" not in session:
        return redirect(url_for("home.home"))
    arquivo = request.files.get("arquivo")

    if not arquivo or not arquivo.filename:
        flash("Selecione um arquivo.")
        return redirect(url_for("upload.upload"))
    upload = Upload(session["usuario_id"])

    if not upload.extensao_permitida(arquivo.filename):
        flash("Tipo de arquivo não permitido.")
        return redirect(url_for("upload.upload"))
    arquivo.seek(0, 2)
    tamanho = arquivo.tell()
    arquivo.seek(0)

    permitido, mensagem = upload.pode_enviar(tamanho)

    if not permitido:
        flash(mensagem)
        return redirect(url_for("upload.upload"))
    upload.salvar(arquivo)
    flash("Arquivo enviado com sucesso.")
    return redirect(url_for("upload.upload"))