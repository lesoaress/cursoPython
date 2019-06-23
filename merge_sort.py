import pytest
import Buscador
def merge_sort(lista): #base da recursao 
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    #chamada recursiva 
    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito

    if not lado_direito:
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])
    
a = [10,20,30,40,50,60]

@pytest.mark.parametrize("lista, valor, esperado", [
    (a, 10, 0),
    (a, 20, 1),
    (a, 30, 2),
    (a, 40, 3),
    (a, 50, 4),
    (a, 60, 5),
    (a, 15, False),
    (a, 70, False),
    (a, -10, False)
    ])

def testa_busca_binaria(lista, valor, esperado):
    assert Buscador.busca_binaria(lista, valor) == esperado
    
