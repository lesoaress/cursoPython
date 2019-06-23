import Ordenador
import random
import time
import Buscador

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x  in range(n)] #lista ordenada
        lista[n//10] = -500
        return lista

    def lista_ordenada(self, n):
        lista = [x for x  in range(n)] #lista ordenada
        return lista

    def compara_ordenadores(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] #clonando uma lista
        lista3 = lista2[:]

        o = Ordenador.Ordenador()

        print("Comparando com listas aleatórias")
        
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("O algoritmo da bolha curta demorou: ", depois-antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("O algoritmo da selação direta demorou: ", depois-antes)

        antes = time.time()
        o.insercao_direta(lista3)
        depois = time.time()
        print("O algoritmo da inserção direta demorou: ", depois-antes)

        print("\nComparando com listas quase ordenadas")

        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:] #clonando uma lista
        lista3 = lista2[:]
        
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("O algoritmo da bolha curta demorou: ", depois-antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("O algoritmo da selação direta demorou: ", depois-antes)

        antes = time.time()
        o.insercao_direta(lista3)
        depois = time.time()
        print("O algoritmo da inserção direta demorou: ", depois-antes)

    def compara_buscadores(self, n):
        b = Buscador.Buscador()
        
        print("Comparando com listas ordenadas")

        lista1 = self.lista_ordenada(n)
        lista2 = lista1[:] #clonando uma lista

        antes = time.time()
        b.busca_sequencial(lista1, x)
        depois = time.time()
        print("O algoritmo da busca sequencial demorou: ", depois-antes)

        antes = time.time()
        b.busca_binaria(lista2, x)
        depois = time.time()
        print("O algoritmo da busca binária demorou: ", depois-antes)

        print("\nComparando com listas aleatórias")
        
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] #clonando uma lista

        antes = time.time()
        b.busca_sequencial(lista1, x)
        depois = time.time()
        print("O algoritmo da busca sequencial demorou: ", depois-antes)

        antes = time.time()
        b.busca_binaria(lista2, x)
        depois = time.time()
        print("O algoritmo da busca binária demorou: ", depois-antes)
        

        
