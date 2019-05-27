def fatorial (n):
    if n < 0:
        return 0
    fat = 1
    i = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat

def test_fatorial_0():
    assert fatorial(0) == 1

def test_fatorial_1():
    assert fatorial(1) == 1

def test_fatorial_negativo():
    assert fatorial(-10) == 0

def test_fatorial_4():
    assert fatorial(4) == 24

def test_fatorial_5():
    assert fatorial(5) == 120
