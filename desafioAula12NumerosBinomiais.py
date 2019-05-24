def fatorial(numero):
    fatorial = 1
    while numero > 1:
        fatorial = fatorial * numero
        numero = numero - 1

    return fatorial
    

def numero_binomial(n, k):
    if n >= k:
        n_fatorial = fatorial(n)
        k_fatorial = fatorial(k)
        n_menos_k_fatorial = fatorial(n-k)
        num_binomial = n_fatorial / (k_fatorial * n_menos_k_fatorial)
        return num_binomial
    else:
        return "O número 'n' precisa ser maior que 'k'!"

n = int(input("Digite o 'n': "))
k = int(input("Digite o 'k': "))

print("O número binomial é: ", numero_binomial(n, k))
