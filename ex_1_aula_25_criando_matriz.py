def cria_matriz(num_linhas, num_colunas, valor):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        matriz.append(linha)
    return mostrar_matriz(num_linhas, num_colunas, matriz)

def mostrar_matriz(num_linhas, num_colunas, matriz):
    for i in range(num_linhas):
        for j in range(num_colunas):
            print(matriz[i][j])
        print("\n")
