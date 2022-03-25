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
from calculadora import soma


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_10(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = ((2, 3, 5), (1, 2, 3), (2, 3, 5))
        for x, y, saida in x_y_saidas:
            with self.subTest(x=x, y=y, saida=saida):
                self.assertEqual(soma(x, y), saida)

    def test_soma_x_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        # isso deve disparar o assert de dentro do def soma, que aqui irá passar o teste!
        with self.assertRaises(AssertionError):
            soma('2', 3)

    def test_soma_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        # isso deve disparar o assert de dentro do def soma, que aqui irá passar o teste!
        with self.assertRaises(AssertionError):
            soma(2, '3')


if __name__ == '__main__':
    unittest.main(verbosity=2)
