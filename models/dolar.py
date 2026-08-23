from peewee import Model, AutoField, CharField, DecimalField, DateTimeField, BooleanField
from datetime import datetime
from database.conexao import db, conectar
from database.crud_base import CrudBase

class Dolar(Model):
    cd_moeda = AutoField()
    valor = DecimalField(max_digits=18, decimal_places=5)
    status = BooleanField(default=True, null=False)
    moeda = CharField(max_length=3, null=False)
    dt_referencia = DateTimeField(null=False)
    dt_atualizacao = DateTimeField(default=datetime.now, null=False)

    class Meta:
        database = db
        table_name = "tb_moeda"

    @staticmethod
    def atual():
        with conectar():
            return (Dolar.select().where((Dolar.status == True) & (Dolar.moeda == "USD")).order_by(Dolar.dt_referencia.desc()).first())

    @staticmethod
    def select_dolar_atual():
        with conectar() as db:
            dolar = db.execute_sql("""SELECT * FROM tb_moeda WHERE status = true AND moeda = 'USD' ORDER BY dt_referencia DESC LIMIT 1;""").fetchone()
            return dolar

class CrudDolar(CrudBase):
    def __init__(self):
        super().__init__(Dolar)