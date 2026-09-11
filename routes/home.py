from flask import Blueprint, render_template, send_from_directory, session, redirect, url_for
from models.moeda import Moeda
from models.ipca import Ipca
from models.selic import Selic
from models.salario import Salario
from models.temperatura import Temperatura
from suporte.download import Download
from datetime import datetime
import calendar

home_bp = Blueprint('home', __name__)

def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

@home_bp.route("/")
def home():

    # Moedas ----------------------------------------------------
    dolar_atual = Moeda.atual("USD")
    euro_atual = Moeda.atual("EUR")
    bitcoin_atual = Moeda.atual("BTC")

    vl_dolar = formatar_real(float(dolar_atual.valor))
    vl_euro = formatar_real(float(euro_atual.valor))
    vl_bitcoin = formatar_real(float(bitcoin_atual.valor))

    dtref_dolar = dolar_atual.dt_referencia.strftime("%d/%m/%Y %H:%M")
    dtref_euro = euro_atual.dt_referencia.strftime("%d/%m/%Y %H:%M")
    dtref_bitcoin = bitcoin_atual.dt_referencia.strftime("%d/%m/%Y %H:%M")

    # IPCA ------------------------------------------------------
    meses = ["Janeiro", "Fevereiro", "Março", "Abril",
             "Maio", "Junho", "Julho", "Agosto",
             "Setembro", "Outubro", "Novembro", "Dezembro"]

    ipca_atual = Ipca.atual()
    vl_ipca = float(ipca_atual.indice)
    vl_ipca_formato = f"{vl_ipca:.2f}%".replace(".", ",")
    dt = ipca_atual.dt_referencia
    dtref_ipca = f"{meses[dt.month - 1]} - {dt.year}"

    # Selic -----------------------------------------------------
    selic_atual = Selic.atual()
    vl_selic = float(selic_atual.indice)
    vl_selic_formato = f"{vl_selic:.2f}%".replace(".", ",")
    dtref_selic = selic_atual.dt_referencia.strftime("%d/%m/%Y")

    # Salário Mínimo --------------------------------------------
    salario_atual = Salario.atual()
    vl_salario = formatar_real(float(salario_atual.vl_salario))
    dtref_salario = salario_atual.dt_referencia.strftime("%d/%m/%Y")

    # Temperaturas ----------------------------------------------
    temperaturas = []

    for registro in Temperatura.atuais():
        temperaturas.append({
            "regiao": registro.regiao,
            "cidade": registro.cidade,
            "temperatura": registro.temperatura,
            "dt_referencia": registro.dt_referencia,
        })

    dt_atual  = datetime.now()
    mes_atual = f"{meses[dt_atual.month - 1]} {dt_atual.year}"
    calendario = calendar.Calendar(firstweekday=6).monthdayscalendar(dt_atual.year, dt_atual.month)

    return render_template(
        "home.html",
        vl_dolar=vl_dolar,
        dtref_dolar=dtref_dolar,
        vl_euro=vl_euro,
        dtref_euro=dtref_euro,
        vl_bitcoin=vl_bitcoin,
        dtref_bitcoin=dtref_bitcoin,
        vl_ipca=vl_ipca_formato,
        dtref_ipca=dtref_ipca,
        vl_selic=vl_selic_formato,
        dtref_selic=dtref_selic,
        vl_salario=vl_salario,
        dtref_salario=dtref_salario,
        temperaturas=temperaturas,
        dt_atual = dt_atual,
        mes_atual = mes_atual,
        calendario = calendario
    )

@home_bp.route("/downloads")
def downloads():
    if "usuario_id" not in session:
        return redirect(url_for("home.home"))
    download = Download(session["usuario_id"])
    arquivos = download.listar()
    return render_template("downloads.html", arquivos=arquivos)

@home_bp.route("/baixar/<path:nome>")
def baixar(nome):
    if "usuario_id" not in session:
        return redirect(url_for("home.home"))
    download = Download(session["usuario_id"])
    caminho = download.caminho(nome)

    if caminho is None:
        return "Arquivo não encontrado.", 404
    return send_from_directory(caminho.parent, caminho.name, as_attachment=True, download_name=nome)

@home_bp.route("/sistema")
def sistema():
    if "usuario_id" not in session:
        return redirect(url_for("home.home"))

    return render_template("sistema.html")
