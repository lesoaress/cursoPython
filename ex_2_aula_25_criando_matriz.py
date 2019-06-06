def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)
        matriz.append(linha)
    return mostrar_matriz(num_linhas, num_colunas, matriz)

def mostrar_matriz(num_linhas, num_colunas, matriz):
    for i in range(num_linhas):
        for j in range(num_colunas):
            print(matriz[i][j], end = ' ')
        print("\n")

def le_matriz():
    lin = int(input("Digite o número de linhas da matriz:"))
    col = int(input("Digite o número de colunas da matriz:"))

    cria_matriz(lin, col)
