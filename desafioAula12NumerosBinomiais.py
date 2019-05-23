def fatorial(numero):
    numero_str = str(numero)
    tamanho_numero = len(numero_str)
    i = 0
    fatorial = 1
    
    if tamanho_numero == 1:
        fatorial = numero
    else:
        while i < tamanho_numero:
            fatorial = fatorial * numero
            numero = numero//10
            i+=1

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
