from flask import Blueprint, render_template
from models.dolar import Dolar
from models.ipca import Ipca

home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def home():

    # Dólar -----------------------------------------------------
    dolar_atual = Dolar.atual()
    vl_dolar = float(dolar_atual.valor)
    dtref_dolar = dolar_atual.dt_referencia

    # IPCA ------------------------------------------------------
    meses = ["Janeiro", "Fevereiro", "Março", "Abril",
            "Maio", "Junho", "Julho", "Agosto",
            "Setembro", "Outubro", "Novembro", "Dezembro"]

    ipca_atual = Ipca.atual()
    vl_ipca = float(ipca_atual.indice)
    vl_ipca_formato = f"{vl_ipca:.2f}%".replace(".", ",")
    dt = ipca_atual.dt_referencia
    dtref_ipca = f"{meses[dt.month - 1]} - {dt.year}"

    # IPCA últimos 6 meses --------------------------------------
    ipca_6_meses = Ipca.ultimos_6m()
    ipca_6_meses.reverse()

# retorno ------------------------------------------------------
    return render_template(
        "home.html",

        vl_dolar=vl_dolar,
        dtref_dolar=dtref_dolar,

        vl_ipca=vl_ipca_formato,
        dtref_ipca=dtref_ipca,
        ipca_6_meses=ipca_6_meses
    )
