from peewee import Model, AutoField, CharField, DecimalField, DateTimeField, BooleanField
from datetime import datetime
from database.conexao import db, conectar
from database.crud_base import CrudBase

class Moeda(Model):
    cd_moeda = AutoField()
    valor = DecimalField(max_digits=18, decimal_places=5)
    status = BooleanField(default=True, null=False)
    moeda = CharField(max_length=5, null=False)
    dt_referencia = DateTimeField(null=False)
    dt_atualizacao = DateTimeField(default=datetime.now, null=False)

    class Meta:
        database = db
        table_name = "tb_moeda"

    @staticmethod
    def atual(codigo):
        with conectar():
            return (Moeda.select().where((Moeda.status == True) & (Moeda.moeda == codigo)).order_by(Moeda.dt_referencia.desc()).first())

    @staticmethod
    def select_dolar_atual():
        with conectar() as db:
            dolares = db.execute_sql("""SELECT DISTINCT ON (moeda) * FROM tb_moeda WHERE status = true AND moeda IN ('USDCC', 'USDCV', 'USDTC', 'USDTV') ORDER BY moeda, dt_referencia DESC;""").fetchall()
            return dolares

class CrudMoeda(CrudBase):
    def __init__(self):
        super().__init__(Moeda)
