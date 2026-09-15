from peewee import Model, AutoField, DecimalField, DateTimeField, BooleanField
from database.conexao import db, conectar


class Ibovespa(Model):
    cd_ibovespa = AutoField()
    pontos = DecimalField(max_digits=12, decimal_places=2)
    variacao = DecimalField(max_digits=8, decimal_places=2)
    variacao_pontos = DecimalField(max_digits=12, decimal_places=2)
    abertura = DecimalField(max_digits=12, decimal_places=2, null=True)
    maxima = DecimalField(max_digits=12, decimal_places=2, null=True)
    minima = DecimalField(max_digits=12, decimal_places=2, null=True)
    fechamento_anterior = DecimalField(max_digits=12, decimal_places=2, null=True)
    status = BooleanField(default=True, null=False)
    dt_referencia = DateTimeField(null=False)
    dt_atualizacao = DateTimeField(null=False)

    class Meta:
        database = db
        table_name = "tb_ibovespa"

    @staticmethod
    def atual():
        with conectar():
            return (Ibovespa.select().where(Ibovespa.status == True).order_by(Ibovespa.dt_referencia.desc()).first())