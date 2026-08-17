import requests

from peewee import Model, AutoField, DecimalField, DateTimeField, BooleanField
from datetime import datetime

from database.conexao import db
from database.conexao import conectar
from database.crud_base import CrudBase

class Dolar(Model):
    cd_dolar = AutoField()
    valor = DecimalField( max_digits=10, decimal_places=2 )
    variacao = DecimalField( max_digits=8, decimal_places=5 )
    status = BooleanField( default=True, null=False )
    dt_referencia = DateTimeField( default=datetime.now, null=False )
    dt_atualizacao = DateTimeField( default=datetime.now, null=False )
    class Meta:
        database = db
        table_name = "tb_dolar"

    @staticmethod
    def buscar():
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get( url, timeout=10 )
        resposta.raise_for_status()
        return resposta.json()

    @staticmethod
    def atual():
        with conectar():
            return (Dolar.select().order_by(Dolar.dt_referencia.desc()).first())

    # Teste: o mesmo resultado que o método dolar_atual() -------------------------------------
    @staticmethod
    def select_dolar_atual():
        with conectar() as db:
            dolar = db.execute_sql("""SELECT * FROM tb_dolar ORDER BY dt_referencia DESC LIMIT 1;""").fetchone()
            return dolar

class CrudDolar(CrudBase):
    def __init__(self):
        super().__init__(Dolar)
