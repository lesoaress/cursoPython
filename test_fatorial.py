def fatorial (n):
    if n < 0:
        return 0
    fat = 1
    i = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat

import pytest

@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (-10, 0),
    (4, 24),
    (5, 120)])
                         
def test_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado
