from peewee import *
from database.conexao import db

class Contato(Model):
    cd_contato = AutoField()
    nm_contato = CharField(max_length=80)
    email = CharField(max_length=120, unique=True)
    celular = CharField(max_length=20, unique=True, null=True)
    comentario = CharField(max_length=200)
    dt_nascimento = DateField(null=True)
    dt_cadastro = DateTimeField()

    class Meta:
        database = db
        table_name = "tb_contato"

    @classmethod
    def inserir(cls, nm_contato, email, celular, comentario, dt_nascimento=None):
        return cls.create(
            nm_contato=nm_contato,
            email=email,
            celular=celular,
            comentario=comentario,
            dt_nascimento=dt_nascimento
        )

    @classmethod
    def buscar_nmcontato(cls, nm_contato):
        return cls.select().where(cls.nm_contato == nm_contato)

    @classmethod
    def buscar_email(cls, email):
        return cls.select().where(cls.email == email)

    @classmethod
    def buscar_celular(cls, celular):
        return cls.select().where(cls.celular == celular)

    @classmethod
    def atualizar(cls, cd_contato, nm_contato, email, celular=None, comentario=None, dt_nascimento=None):
        return (cls.update(
                nm_contato=nm_contato,
                email=email,
                celular=celular,
                comentario=comentario,
                dt_nascimento=dt_nascimento
                ).where(cls.cd_contato == cd_contato).execute())

    @classmethod
    def excluir(cls, cd_contato):
        return cls.delete().where(cls.cd_contato == cd_contato).execute()