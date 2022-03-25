import requests


class Pessoa:
    def __init__(self, nome, sobrenome):
        assert isinstance(nome, str), 'Nome precisa ser uma string'
        assert isinstance(sobrenome, str), 'Sobrenome precisa ser uma string'
        self.nome = nome
        self.sobrenome = sobrenome
        self.dados_obtidos = False

    def obter_dados(self):
        self.dados_obtidos = False
        resposta = requests.get('')
        if resposta.status_code == 200:
            self.dados_obtidos = True
            return 200
        elif resposta.status_code == 404:
            return 404
        else:
            return 500
