"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool (false)
    API:
        obter_dados -> method
            ok
            404
            Falha ao conectar com o servidor

            dados_obtidos se torta true se for sucesso
"""
# Como estamos em nivel de pastas diferentes das nossas classes e métodos,
#   precisamos manipular o path para importar as classes e métodos.
#   Para isso, utilizamos o método sys.path.append() que adiciona um caminho ao path.
try:
    import sys
    import os
    sys.path.append(os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../src')))
except:
    raise

import unittest
from pessoa import Pessoa
from unittest.mock import patch


class TestPessoa(unittest.TestCase):
    # setUp usado antes de inicializar o teste pelo proprio unittest
    def setUp(self):
        self.pessoa = Pessoa('Eliezer', 'Santos')

    # Valida_Tipagem
    def test_pessoa_attr_nome_eh_str(self):
        self.assertIsInstance(self.pessoa.nome, str)

    def test_pessoa_attr_sobrenome_eh_str(self):
        self.assertIsInstance(self.pessoa.sobrenome, str)

    # Valida_Dados
    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa.nome, 'Eliezer')

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.pessoa.sobrenome, 'Santos')

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.pessoa.dados_obtidos)

    def test_pessoa_obter_dados_retorna_200(self):
        # Mockando a resposta do servidor para retornar 200
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            self.assertEqual(self.pessoa.obter_dados(),
                             mock_get.return_value.status_code)
            self.assertTrue(self.pessoa.dados_obtidos)

    def test_pessoa_obter_dados_retorna_404(self):
        # Mockando a resposta do servidor para retornar 404
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 404
            self.assertEqual(self.pessoa.obter_dados(),
                             mock_get.return_value.status_code)
            self.assertFalse(self.pessoa.dados_obtidos)

    def test_pessoa_obter_dados_retorna_falha_conexao(self):
        # Mockando a resposta do servidor para retornar falha de conexao
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 500
            self.assertEqual(self.pessoa.obter_dados(),
                             mock_get.return_value.status_code)
            self.assertFalse(self.pessoa.dados_obtidos)


if __name__ == '__main__':
    unittest.main(verbosity=2)
