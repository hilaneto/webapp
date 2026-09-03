from models.download import Download

@app.route("/downloads")
def downloads():
    arquivos = Download.listar()
    return render_template("downloads.html", arquivos=arquivos)
