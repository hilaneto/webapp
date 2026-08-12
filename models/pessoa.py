
from peewee import Model, AutoField, CharField, IntegerField, BooleanField, DateTimeField, DateField
from datetime import datetime, date
from database.conexao import db
from database.crud_base import CrudBase

class Pessoa(Model):
    cd_pessoa = AutoField()
    nm_pessoa = CharField(max_length=100)
    cpf = CharField(max_length=11, unique=True)
    dt_nascimento = DateField(default=date.today)
    sexo = CharField(max_length=1)
    fl_ativo = BooleanField(default=True)
    observacao = CharField(max_length=100)
    dt_atualizacao = DateTimeField(default=datetime.now, null=False)
    
    class Meta:
        database = db
        table_name = "tb_pessoa"

class CrudPessoa(CrudBase):
    def __init__(self):
        super().__init__(Pessoa)
