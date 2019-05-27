import math

def calcula_delta(a, b, c):
    return b**2 - 4*a*c

def calcula_raizes(a, b, delta):
    raiz = (-b + math.sqrt(delta))/(2*a)
    raiz2 = (-b - math.sqrt(delta))/(2*a)
    return raiz, raiz2
    
def calcula_funcao(a, b, c):
    delta = calcula_delta(a, b, c)
    if delta < 0:
       print("Não existe raiz real para essa expressão!")
    else:
        if delta == 0:
            print("A única raiz é: ", calcula_raizes(a, b, delta))
        else:
            print("Raiz(es) = ", calcula_raizes(a, b, delta))

def main():
    a_digitado = int(input("Insira o 'a' da equação: "))
    b_digitado = int(input("Insira o 'b' da equação: "))
    c_digitado = int(input("Insira o 'c' da equação: "))
    calcula_funcao(a_digitado,b_digitado,c_digitado)






        

    
