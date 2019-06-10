import Bhaskara
import pytest

class TestBhaskara:

    @pytest.mark.parametrize("entrada, esperado", [
        ((1,0,0), (1,0)), 
        ((1, -5, 6), (2, 3, 2)),
        ((10, 10, 10), 0),
        ((10, 20, 10), (1,-1))
        ]
        
    @pytest.fixture
    def b(self):
        return Bhaskara.Bhaskara()
    
    def test_raiz(self, b, entrada, esperado):
        assert b.calcula_raizes(entrada) == esperado

    
