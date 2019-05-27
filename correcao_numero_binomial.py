def fatorial(n):
    fat = 1
    while n > 1:
        fat = fat * n
        n = n - 1
    return fat

def numero_binomial(n, k):
    if n >= k:
        return fatorial(n)/(fatorial(k) * fatorial(n-k))
    else:
        return "'n' tem que ser maior que 'k'"

def testa_fatorial():
    
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")
        
    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")

    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")

    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")

def testa_numero_binomial():
    if numero_binomial(5,3) == 10:
        print("Funciona para 5 e 3")
    else:
        print("Não funciona para 5 e 3")

    if numero_binomial(8, 4) == 70:
        print("Funciona para 8 e 4")
    else:
        print("Não funciona para 8 e 4") 
        
