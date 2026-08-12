
from datetime import datetime, timedelta

class CrudBase:

    def __init__(self, model):
        self.model = model

    # Método privado =====================================================
    def _aplicar_filtros(self, consulta, filtros=None):
        if not filtros:
            return consulta
        for campo, valor in filtros.items():
            if not hasattr(self.model, campo):
                raise AttributeError(f"O campo '{campo}' não existe em {self.model.__name__}.")
            consulta = consulta.where(getattr(self.model, campo) == valor)
        return consulta

    # Buscar =====================================================
    def buscar(self, **filtros):
        return self._aplicar_filtros(self.model.select(),filtros)

    # Contar =====================================================
    def contar(self, **filtros):
        return self.buscar(**filtros).count()

    # Buscar por período ==========================================
    def buscar_periodo(self, busca: dict):
        if not hasattr(self.model, "dt_atualizacao"):
            raise AttributeError(f"{self.model.__name__} não possui dt_atualizacao.")
        if "data_inicial" not in busca:
            raise ValueError("Informe data_inicial.")
        data_inicial = busca["data_inicial"]
        data_final = busca.get("data_final", data_inicial)
        inicio = datetime.combine(data_inicial,datetime.min.time())
        fim = datetime.combine(data_final + timedelta(days=1),datetime.min.time())
        return self.model.select().where(
            (self.model.dt_atualizacao >= inicio) &
            (self.model.dt_atualizacao < fim))

    # Inserir =====================================================
    def inserir(self, **dados):
        return self.model.create(**dados)

    # Alterar =====================================================
    def alterar(self, filtros: dict, **dados):
        if not filtros:
            raise ValueError("Informe pelo menos um filtro.")
        if not dados:
            raise ValueError("Informe os dados para atualização.")
        if hasattr(self.model, "dt_atualizacao"):
            dados["dt_atualizacao"] = datetime.now()
        consulta = self.model.update(**dados)
        consulta = self._aplicar_filtros(consulta,filtros)
        return consulta.execute()

    # Excluir =====================================================
    def excluir(self, **filtros):
        if not filtros:
            raise ValueError("Informe pelo menos um filtro.")
        consulta = self.model.delete()
        consulta = self._aplicar_filtros(consulta,filtros)
        return consulta.execute()

    # Desativar =====================================================
    def desativar(self, **filtros):
        if not hasattr(self.model, "fl_ativo"):
            raise AttributeError(f"{self.model.__name__} não possui fl_ativo.")
        return self.alterar(filtros,fl_ativo=False)
