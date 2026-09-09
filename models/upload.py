from pathlib import Path
from werkzeug.utils import secure_filename

class Upload:
    PASTA_DOWNLOADS = Path(__file__).resolve().parent.parent / "downloads"
    LIMITE_ARQUIVO = 50 * 1024 * 1024
    LIMITE_USUARIO = 500 * 1024 * 1024
    EXTENSOES_PERMITIDAS = {".pdf", ".xlsx", ".xls", ".csv", ".txt", ".jpg", ".jpeg", ".png", ".zip"}

    def __init__(self, cd_usuario):
        self.cd_usuario = cd_usuario
        self.prefixo = f"us{cd_usuario:06d}_"

    def arquivos(self):
        if not self.PASTA_DOWNLOADS.exists():
            return []

        return [arquivo
                for arquivo in self.PASTA_DOWNLOADS.iterdir()
                if arquivo.is_file() and arquivo.name.startswith(self.prefixo)
               ]

    def uso(self):
        return sum(arquivo.stat().st_size for arquivo in self.arquivos())

    def disponivel(self):
        return max(0, self.LIMITE_USUARIO - self.uso())

    def nome_arquivo(self, nome_original):
        nome = secure_filename(nome_original)
        return self.prefixo + nome

    def extensao_permitida(self, nome_original):
        extensao = Path(nome_original).suffix.lower()
        return extensao in self.EXTENSOES_PERMITIDAS

    def pode_enviar(self, tamanho):
        return tamanho <= self.LIMITE_ARQUIVO and self.uso() + tamanho <= self.LIMITE_USUARIO

    def salvar(self, arquivo):
        self.PASTA_DOWNLOADS.mkdir(parents=True, exist_ok=True)
        nome = self.nome_arquivo(arquivo.filename)
        caminho = self.PASTA_DOWNLOADS / nome
        arquivo.save(caminho)
        return caminho
