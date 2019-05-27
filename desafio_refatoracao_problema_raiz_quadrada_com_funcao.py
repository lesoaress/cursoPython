import math

def calcula_delta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

def calcula_raizes(a, b, delta):
    raiz = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)
    return raiz, raiz2
    
def calcula_funcao(a, b, c):
    if calcula_delta(a, b, c) < 0:
        return "Não existe raiz real para essa expressão!"
    else:
        if calcula_delta(a, b, c) == 0:
            return "A única raiz é: ", calcula_raizes(a, b, calcula_delta(a, b, c))
        else:
            return "Raiz(es) = ", calcula_raizes(a, b, calcula_delta(a, b, c))

a = int(input("Insira o 'a' da equação: "))
b = int(input("Insira o 'b' da equação: "))
c = int(input("Insira o 'c' da equação: "))

print(calcula_funcao(a, b, c))




        

    
