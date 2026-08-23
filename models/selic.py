from peewee import Model, AutoField, DecimalField, DateTimeField, DateField, BooleanField
from datetime import datetime
from database.conexao import db
from database.conexao import conectar
from database.crud_base import CrudBase

class Selic(Model):
    cd_selic = AutoField()
    indice = DecimalField(max_digits=8, decimal_places=5)
    status = BooleanField(default=True, null=False)
    dt_referencia = DateField(null=False)
    dt_atualizacao = DateTimeField(default=datetime.now, null=False)    
    
    class Meta:
        database = db
        table_name = "tb_selic"

    @staticmethod
    def atual():
        with conectar():
            return (Selic.select().where(Selic.status == True).order_by(Selic.dt_referencia.desc()).first())

    @staticmethod
    def ultimos_6m():
        with conectar():
            return list(Selic.select().where(Selic.status == True).order_by(Selic.dt_referencia.desc()).limit(6))

class CrudSelic(CrudBase):
    def __init__(self):
        super().__init__(Selic)
