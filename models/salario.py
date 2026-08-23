from peewee import Model, AutoField, DecimalField, DateTimeField, DateField, BooleanField
from datetime import datetime
from database.conexao import db
from database.conexao import conectar
from database.crud_base import CrudBase

class Salario(Model):
    cd_salario = AutoField()
    vl_salario = DecimalField(max_digits=8, decimal_places=2)
    status = BooleanField(default=True, null=False)
    dt_referencia = DateField(null=False)
    dt_atualizacao = DateTimeField(default=datetime.now, null=False)    
    
    class Meta:
        database = db
        table_name = "tb_salariominimo"

    @staticmethod
    def atual():
        with conectar():
            return (Salario.select().where(Salario.status == True).order_by(Salario.dt_referencia.desc()).first())

    @staticmethod
    def ultimos_6m():
        with conectar():
            return list(Salario.select().where(Salario.status == True).order_by(Salario.dt_referencia.desc()).limit(6))

class CrudSalario(CrudBase):
    def __init__(self):
        super().__init__(Salario)
