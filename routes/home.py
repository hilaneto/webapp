from flask import Blueprint, render_template
from suporte.dolar import Dolar
from datetime import datetime

home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def home():
    dados = Dolar.buscar()
    dolar = dados["USDBRL"]
    valor = float(dolar["bid"])
    variacao = float(dolar["pctChange"])
    data = datetime.strptime( dolar["create_date"], "%Y-%m-%d %H:%M:%S" )
    atualizacao = data.strftime("%d/%m/%Y %H:%M")

    return render_template(
        "home.html",
        dolar_valor=valor,
        dolar_variacao=variacao,
        dolar_atualizacao=atualizacao
    )
