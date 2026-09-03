from pathlib import Path
from datetime import datetime

class Download:
    PASTA = Path("/var/www/html/publico/instalacao")

    @classmethod
    def listar(cls):
        arquivos = []

        for arquivo in sorted(cls.PASTA.iterdir()):
            if arquivo.is_file():
                arquivos.append({
                    "nome": arquivo.name,
                    "tamanho": arquivo.stat().st_size,
                    "data": datetime.fromtimestamp(arquivo.stat().st_mtime).strftime("%d/%m/%Y %H:%M")
                })

        return arquivos