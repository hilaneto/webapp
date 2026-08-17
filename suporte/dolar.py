import requests

class Dolar:
    @staticmethod
    def buscar():
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        return resposta.json()