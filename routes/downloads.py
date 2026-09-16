from flask import Blueprint, render_template, session, redirect, url_for, send_from_directory
from suporte.download import Download

download_bp = Blueprint("download", __name__)

@download_bp.route("/downloads")
def downloads():
    if "usuario_id" not in session:
        return redirect(url_for("home.home"))

    download = Download(session["usuario_id"])
    arquivos = download.listar()

    return render_template("downloads.html", arquivos=arquivos)


@download_bp.route("/downloads/<path:nome>")
def baixar(nome):
    if "usuario_id" not in session:
        return redirect(url_for("home.home"))

    download = Download(session["usuario_id"])
    caminho = download.caminho(nome)

    if caminho is None:
        return "Arquivo não encontrado.", 404

    return send_from_directory(
        caminho.parent,
        caminho.name,
        as_attachment=True,
        download_name=nome
    )
