import Bhaskara

class TestBhaskara:
    def testa_uma_raiz(self):
        b = Bhaskara()
        assert b.calcula_raizes(1, 0, 0) == (1, 0) 
