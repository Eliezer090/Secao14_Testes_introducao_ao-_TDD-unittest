"""
1- receber um numero inteiro
2- saber se o numero é multiplo de 3 e 5
    Retorna:
        Bacon com ovos
3- Saber se um numero é multiplo somente de 3
    Retorna:
        Bacon
4- Saber se um numero é multiplo somente de 5
    Retorna:
        Ovos
5- Saber se um numero NÃO é multiplo de 3 e 5:
    Retorna:
        Passa fome
"""


def bacon_com_ovos(n):
    assert isinstance(n, int), 'O numero não é inteiro'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    elif n % 3 == 0:
        return 'Bacon'
    elif n % 5 == 0:
        return 'Ovos'
    return 'Passa fome'
