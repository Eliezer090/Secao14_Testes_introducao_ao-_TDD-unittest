
def soma(x, y):
    """Soma x e y
    >>> soma(2, 3)
    5
    >>> soma(1, 2)
    3
    >>> soma('2', '3')
    '23'
    """
    assert isinstance(x, (int, float)) and isinstance(
        y, (int, float)), 'x e y devem ser números'
    return x + y


# esta é uma maneira de testar nao é a melhor
if __name__ == '__main__':
    import doctest
    doctest.testmod()
