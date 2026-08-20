import requests
from peewee import Model, AutoField, DecimalField, DateTimeField, DateField, BooleanField
from datetime import datetime, timedelta
from database.conexao import db
from database.conexao import conectar
from database.crud_base import CrudBase
from decimal import Decimal

class Ipca(Model):
    cd_ipca = AutoField()
    indice = DecimalField(max_digits=8, decimal_places=5)
    status = BooleanField(default=True, null=False)
    dt_referencia = DateField(null=False)
    dt_atualizacao = DateTimeField(default=datetime.now, null=False)    
    
    class Meta:
        database = db
        table_name = "tb_ipca"

    @staticmethod
    def atual():
        with conectar():
            return (Ipca.select().where(Ipca.status == True).order_by(Ipca.dt_referencia.desc()).first())

    @staticmethod
    def ultimos_6m():
        with conectar():
            return list(Ipca.select().where(Ipca.status == True).order_by(Ipca.dt_referencia.desc()).limit(6))

class CrudIpca(CrudBase):
    def __init__(self):
        super().__init__(Ipca)
