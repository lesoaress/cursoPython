class Matriz:
    
    def cria_matriz(self, num_linhas, num_colunas, valor):
        matriz = []
        for i in range(num_linhas):
            linha = []
            for j in range(num_colunas):
                linha.append(valor)
            matriz.append(linha)
        return matriz

    def mostrar_matriz(self, num_linhas, num_colunas, matriz):
        for i in range(num_linhas):
            for j in range(num_colunas):
                print(matriz[i][j])
            print("\n")
