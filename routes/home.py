from flask import Blueprint, render_template
from models.dolar import Dolar

home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def home():
    dolar_atual = Dolar.atual()

    valor = float(dolar_atual.valor)
    variacao = float(dolar_atual.variacao)
    dtreferencia = dolar_atual.dt_referencia

    return render_template("home.html",
                            dolar_valor = valor,
                            dolar_variacao = variacao,
                            dolar_dtreferencia = dtreferencia
                           )
