from datetime import datetime
from peewee import Model, AutoField, CharField, DecimalField, DateTimeField, BooleanField, ForeignKeyField
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
    cd_temperatura = AutoField()
    capital = ForeignKeyField(Capital, field=Capital.cd_capital, column_name="cd_capital", backref="temperaturas")
    temperatura = DecimalField(max_digits=5, decimal_places=2, null=True)
    dt_referencia = DateTimeField()
    dt_atualizacao = DateTimeField(default=datetime.now)
    status = BooleanField(default=True)

    class Meta:
        database = db
        table_name = "tb_temperatura"

    @classmethod
    def atuais(cls):
        with conectar():
            dados = list(cls.select(cls,Capital).join(Capital).distinct(Capital.cd_capital).order_by(Capital.cidade,cls.dt_referencia.desc()))

        return dados
