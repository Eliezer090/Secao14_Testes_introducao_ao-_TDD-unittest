"""
Utilizando o TDD - Test Driven Development(Teste-Desenvolvimento-Teste)

red
1- Criar o teste e ver falhar

Gren
2- Criar o teste e ver passar

Refactor
3- Melhorar o código
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
from baconcomovos import bacon_com_ovos


class TestBaconComovos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assert_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('5')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_receber_int_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60, 75, 90, 105)
        saidas = ('Bacon com ovos', 'Bacon com ovos', 'Bacon com ovos',
                  'Bacon com ovos', 'Bacon com ovos', 'Bacon com ovos', 'Bacon com ovos')
        for entrada, saida in zip(entradas, saidas):
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_bacon_se_receber_int_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21, 24, 27)
        saidas = ('Bacon', 'Bacon', 'Bacon', 'Bacon',
                  'Bacon', 'Bacon', 'Bacon', 'Bacon', 'Bacon')
        for entrada, saida in zip(entradas, saidas):
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_ovos_se_receber_int_multiplo_de_5(self):
        entradas = (5, 10, 20,  25,  35, 40,  50)
        saidas = ('Ovos', 'Ovos', 'Ovos', 'Ovos', 'Ovos',
                  'Ovos', 'Ovos', 'Ovos', 'Ovos', 'Ovos')
        for entrada, saida in zip(entradas, saidas):
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)

    def test_bacon_com_ovos_deve_retornar_passa_fome_se_receber_int_nao_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8, 11, 14, 17)
        saidas = ('Passa fome', 'Passa fome', 'Passa fome', 'Passa fome',
                  'Passa fome', 'Passa fome', 'Passa fome', 'Passa fome', 'Passa fome')
        for entrada, saida in zip(entradas, saidas):
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida)


if __name__ == '__main__':
    unittest.main(verbosity=2)
