
from database.conexao import conectar
from models.dolar import CrudDolar, Dolar
from peewee import IntegrityError
from datetime import datetime

dados_api = Dolar.buscar()
dolar_api = dados_api["USDBRL"]

dt_referencia = datetime.strptime( dolar_api["create_date"], "%Y-%m-%d %H:%M:%S" )

dados = {"valor": dolar_api["bid"],
         "variacao": dolar_api["pctChange"],
         "dt_referencia": dt_referencia,
         "dt_atualizacao": datetime.now()
        }

with conectar():
    try:
        crud = CrudDolar()
        resultado = crud.inserir(**dados)
        print(resultado)
    except TypeError as erro:
        print(f"Erro de tipo: {erro}")
    except IntegrityError as erro:
        print(f"Erro do PostgreSQL: {erro}")        