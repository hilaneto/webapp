
from peewee import Model, AutoField, CharField, IntegerField, BooleanField, DateTimeField
from datetime import datetime
from database.conexao import db
from database.crud_base import CrudBase

class Usuario(Model):
    cd_usuario = AutoField()
    nm_usuario = CharField(max_length=45)
    login = CharField(max_length=30, unique=True)
    senha = CharField(max_length=60)
    cpf = CharField(max_length=11, unique=True)
    cd_permissao = IntegerField()
    email = CharField(max_length=50, null=True)
    fl_ativo = BooleanField(default=True)
    dt_atualizacao = DateTimeField(default=datetime.now, null=False)

    class Meta:
        database = db
        table_name = "tb_usuario"

class CrudUsuario(CrudBase):
    def __init__(self):
        super().__init__(Usuario)
        