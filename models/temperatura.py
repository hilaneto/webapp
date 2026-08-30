from peewee import Model, AutoField, DecimalField, DateTimeField, BooleanField, CharField
from datetime import datetime
from database.conexao import db, conectar
from database.crud_base import CrudBase

class Temperatura(Model):
    cd_temperatura = AutoField()
    regiao = CharField(max_length=20)
    cidade = CharField(max_length=50)
    temperatura = DecimalField(max_digits=5, decimal_places=2, null=True)
    dt_referencia = DateTimeField(null=True)
    dt_atualizacao = DateTimeField(default=datetime.now)
    status = BooleanField(default=True)

    class Meta:
        database = db
        table_name = "tb_temperatura"

    @staticmethod
    def atuais():
        with conectar():
            return list(
                Temperatura
                .select()
                .distinct(Temperatura.cidade)
                .order_by(
                    Temperatura.cidade,
                    Temperatura.dt_referencia.desc()))

class CrudTemperatura(CrudBase):

    def __init__(self):
        super().__init__(Temperatura)