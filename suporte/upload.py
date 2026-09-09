from pathlib import Path
from werkzeug.utils import secure_filename

class Upload:
    PASTA_DOWNLOADS = Path(__file__).resolve().parent.parent / "downloads"
    LIMITE_ARQUIVO = 50 * 1024 * 1024      # 50 MB
    LIMITE_USUARIO = 500 * 1024 * 1024     # 500 MB
    EXTENSOES_PERMITIDAS = {".pdf", ".xlsx", ".xls", ".csv", ".txt", ".jpg", ".jpeg", ".png", ".zip"}

    def __init__(self, cd_usuario):
        self.cd_usuario = cd_usuario
        self.prefixo = f"us{cd_usuario:06d}_"

    def arquivos_usuario(self):
        if not self.PASTA_DOWNLOADS.exists():
            return []

        return [arquivo
                for arquivo in self.PASTA_DOWNLOADS.iterdir()
                if arquivo.is_file() and arquivo.name.startswith(self.prefixo)
               ]

    def uso_usuario(self):
        return sum(arquivo.stat().st_size for arquivo in self.arquivos_usuario())

    def espaco_disponivel(self):
        return max(0, self.LIMITE_USUARIO - self.uso_usuario())

    def extensao_permitida(self, nome_arquivo):
        extensao = Path(nome_arquivo).suffix.lower()
        return extensao in self.EXTENSOES_PERMITIDAS

    def gerar_nome(self, nome_original):
        nome = secure_filename(nome_original)
        return self.prefixo + nome

    def pode_enviar(self, tamanho):
        if tamanho > self.LIMITE_ARQUIVO:
            return False, "Arquivo excede o limite permitido."

        if self.uso_usuario() + tamanho > self.LIMITE_USUARIO:
            return False, "Limite de armazenamento do usuário excedido."
        return True, ""

    def salvar(self, arquivo):
        self.PASTA_DOWNLOADS.mkdir(parents=True, exist_ok=True)
        nome_arquivo = self.gerar_nome(arquivo.filename)
        caminho = self.PASTA_DOWNLOADS / nome_arquivo
        arquivo.save(caminho)
        return caminho