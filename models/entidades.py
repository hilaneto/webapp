
from peewee import (Model, AutoField, CharField, IntegerField, BooleanField, DateTimeField, DateField)
from datetime import datetime, date
from database.conexao import db
from database.crud_base import CrudBase

# Models ==========================================================================================
class Usuario(Model):
    cd_usuario = AutoField()
    nm_usuario = CharField(max_length=45)
    login = CharField(max_length=30, null=True, unique=True)
    senha = CharField(max_length=60)
    cpf = CharField(max_length=11, unique=True)
    cd_permissao = IntegerField()
    email = CharField(max_length=50, null=True, unique=True)
    fl_ativo = BooleanField(default=True)
    dt_atualizacao = DateTimeField(default=datetime.now, null=False)

    class Meta:
        database = db
        table_name = "tb_usuario"

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

                
# Cruds ========================================================================================
class CrudUsuario(CrudBase):
    def __init__(self):
        super().__init__(Usuario)

class CrudPessoa(CrudBase):
    def __init__(self):
        super().__init__(Pessoa)
