from flask import Blueprint, render_template, session, redirect, url_for
from suporte.download import Download

download_bp = Blueprint("download", __name__)

@download_bp.route("/downloads")
def downloads():
    if "cd_usuario" not in session:
        return redirect(url_for("login"))

    download = Download(session["cd_usuario"])
    arquivos = download.listar()

    return render_template("downloads.html", arquivos=arquivos)
