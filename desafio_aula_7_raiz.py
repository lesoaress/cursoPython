a = int(input("Insira o 'a' da equação: "))
b = int(input("Insira o 'b' da equação: "))
c = int(input("Insira o 'c' da equação: "))

import math

delta = b**2 - 4*a*c

if delta < 0:
    print("Não existe raiz real para essa expressão!")
else:
    raiz = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)
    if delta == 0:
        print("A única raiz é: ", raiz)
    else:
        print("Raiz(es) = ", raiz, "e ", raiz2)
        

    
