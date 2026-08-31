from datetime import datetime
from peewee import Model, AutoField, CharField, DecimalField, DateTimeField, BooleanField, ForeignKeyField, IntegerField
from database.conexao import db, conectar


class Capital(Model):
    cd_capital = AutoField()
    cidade = CharField(max_length=50)
    cidade_busca = CharField(max_length=50)
    uf = CharField(max_length=2)
    regiao = CharField(max_length=20)
    cd_ibge = CharField(max_length=7)

    class Meta:
        database = db
        table_name = "tb_capital"


class Temperatura(Model):
    cd_capital = IntegerField()
    cidade = CharField()
    uf = CharField()
    regiao = CharField()
    temperatura = DecimalField(null=True)
    dt_referencia = DateTimeField()

    class Meta:
        database = db
        table_name = "vw_temperatura_atual"
        primary_key = False

    @classmethod
    def atuais(cls):
        with conectar():
            dados = list(cls.select().order_by(cls.cidade))

        return dados