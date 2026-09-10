from peewee import *
from werkzeug.security import generate_password_hash, check_password_hash
from database.conexao import db, conectar

class Usuario(Model):
    cd_usuario = BigAutoField()
    login = CharField(max_length=100, unique=True)
    senha_hash = TextField()
    ativo = BooleanField(default=True)
    dt_cadastro = DateTimeField(null=True)
    dt_atualizacao = DateTimeField(null=True)
    dt_ultimo_acesso = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = "tb_usuario"

    @staticmethod
    def normalizar_login(login):
        return login.strip().lower()

    @classmethod
    def criar(cls, login, senha):
        login = cls.normalizar_login(login)
        senha_hash = generate_password_hash(senha)
        with conectar():
            return cls.create(login=login, senha_hash=senha_hash)

    @classmethod
    def buscar_login(cls, login):
        login = cls.normalizar_login(login)
        with conectar():
            return cls.get_or_none(cls.login == login)

    @classmethod
    def buscar_cdusuario(cls, cd_usuario):
        with conectar():
            return (Usuario.select().where(Usuario.cd_usuario == cd_usuario).order_by(Usuario.dt_atualizacao.desc()).first())

    @classmethod
    def autenticar(cls, login, senha):
        login = cls.normalizar_login(login)
        with conectar():
            usuario = cls.get_or_none((cls.login == login) & (cls.ativo == True))
            if usuario and check_password_hash(usuario.senha_hash, senha):
                return usuario
            return None
