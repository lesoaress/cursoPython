import Ordenador
import pytest
import ContaTempos

class TestOrdenador:
    @pytest.fixture
    def o (self):
        return Ordenador.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = ContaTempos.ContaTempos()
        return c.lista_quase_ordenada(100)
    
    @pytest.fixture
    def l_aleatoria(self):
        c = ContaTempos.ContaTempos()
        return c.lista_aleatoria(100)        

    def esta_ordenada(self, lista):
        fim = len(lista) - 1 
        for i in range(fim):
            if lista[i] > lista[i+1]:
                return False
        return True
    
    def test_bolha_curta_list_aleatoria(self, o, l_aleatoria):
        o.bolha_curta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_selecao_direta_list_aleatoria(self, o, l_aleatoria):
        o.bolha_curta(l_aleatoria)
        assert self.esta_ordenada(l_aleatoria)

    def test_bolha_curta_list_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)

    def test_selacao_direta_list_quase(self, o, l_quase):
        o.bolha_curta(l_quase)
        assert self.esta_ordenada(l_quase)
        
