from flask import Blueprint, render_template
from models.moeda import Moeda
from models.ipca import Ipca
from models.selic import Selic
from models.salario import Salario
from models.temperatura import Temperatura

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

    # Selic ------------------------------------------------------
    selic_atual = Selic.atual()
    vl_selic = float(selic_atual.indice)
    vl_selic_formato = f"{vl_selic:.2f}%".replace(".", ",")
    dtref_selic = selic_atual.dt_referencia.strftime("%d/%m/%Y")

    # Salário Mínimo -----------------------------------------------
    salario_atual = Salario.atual()
    vl_salario = formatar_real(float(salario_atual.vl_salario))
    dtref_salario = salario_atual.dt_referencia.strftime("%d/%m/%Y")

    # Temperaturas ----------------------------------------------
    dados_temperatura = Temperatura.atuais()

    temperaturas = []

    for registro in dados_temperatura:
        temperaturas.append({
            "regiao": registro.capital.regiao,
            "cidade": registro.capital.cidade,
            "temperatura": (
                f"{float(registro.temperatura):.1f}°C".replace(".", ",")
                if registro.temperatura is not None
                else "--"
            ),
            "dt_referencia": (
                registro.dt_referencia.strftime("%d/%m/%Y %H:%M")
                if registro.dt_referencia
                else "--"
            ),
            "status": registro.status
        })

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

        temperaturas=temperaturas
        )
        
 