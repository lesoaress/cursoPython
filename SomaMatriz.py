import Matriz

def main():
        A_digitado = input("Digite o número de linhas")
        B_digitado = input("Digite o número de colunas")
        matriz = SomaMatriz.soma_matrizes(A_digitado, B_digitado)
        print(matriz)

class SomaMatriz:
    
    def soma_matrizes(self, A, B):
        self.num_lin = len(A)
        self.num_col = len(A[0])
        self.C = Matriz.cria_matriz(int(self.num_lin), int(self.num_col), 0)

        for lin in range(self.num_lin): #percorre as linhas da matriz
            for col in range(self.num_col): #percorre as colunas da matriz
                self.C[lin][col] = A[lin][col] + B[lin][col]

        return self.C

main()
