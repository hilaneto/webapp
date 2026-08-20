
from peewee import IntegrityError
from database.conexao import conectar
from models.dolar import Dolar, CrudDolar
from datetime import date, datetime

def atualizar_dolar():

    try:
        dados_api = Dolar.buscar()
        dolar_api = dados_api["USDBRL"]
        dados = {"valor": dolar_api["valor"],
                 "dt_referencia": date.strptime(dolar_api["data"],
                 "%Y-%m-%d %H:%M:%S"),
                 "dt_atualizacao": datetime.now(),
                 "status": True}

    except Exception as erro:
        dados = {"valor": 0,
                "dt_referencia": datetime.now(),
                "dt_atualizacao": datetime.now(),
                "status": False}
        print(f"Erro ao atualizar dólar: {erro}")

    with conectar():
        crud = CrudDolar()
        crud.inserir(**dados)

if __name__ == "__main__":
    atualizar_dolar()