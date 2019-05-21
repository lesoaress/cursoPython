a = int(input("Insira o 'a' da equação: "))
b = int(input("Insira o 'b' da equação: "))
c = int(input("Insira o 'c' da equação: "))

import math

delta = math.sqrt(b**2 - 4*a*c)

if delta < 0:
    print("Não existe raiz real para essa expressão!")
    
raiz = (-b + delta)/(2*a)
raiz2 = (-b - delta)/(2*a)

print("Raiz(es) = ", raiz, "e ", raiz2)

    
