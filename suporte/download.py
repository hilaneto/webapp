from pathlib import Path

class Download:
    PASTA_DOWNLOADS = Path(__file__).resolve().parent.parent / "downloads"

    def __init__(self, usuario_id):
        self.usuario_id = usuario_id
        self.prefixo = f"us{usuario_id:06d}_"

    def listar(self):
        if not self.PASTA_DOWNLOADS.exists():
            return []

        arquivos = []

        for arquivo in self.PASTA_DOWNLOADS.iterdir():
            if arquivo.is_file() and arquivo.name.startswith(self.prefixo):
                arquivos.append({
                    "nome": arquivo.name.removeprefix(self.prefixo),
                    "tamanho": arquivo.stat().st_size
                })

        return arquivos

    def caminho(self, nome):
        nome_fisico = self.prefixo + nome
        caminho = self.PASTA_DOWNLOADS / nome_fisico

        if not caminho.is_file():
            return None

        return caminho
