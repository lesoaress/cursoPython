def multiplicar_mat(A, B):
    num_lin_A, num_colunas_A = len(A), len(A[0])
    num_lin_B, num_colunas_B = len(B), len(B[0])
    assert num_colunas_A == num_lin_B

    C = []
    for linha in range(num_lin_A):
        #Começando uma nova linha
        C.append([])
        for coluna in range(num_colunas_B):
            #Adicionando uma nova coluna na linha
            C[linha].append(0)
            for k in range(num_colunas_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6]]
    B = [[1,2],[3,4],[5,6]]
    print(multiplicar_mat(A, B))
