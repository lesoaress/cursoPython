import math

class Bhaskara:
    def calcula_delta(self, a, b, c):
        return b**2 - 4*a*c
    
    def calcula_raizes(self, a, b, c):
        delta = self.calcula_delta(a, b, c)
        if delta < 0:
           return 0
        else:
            if delta == 0:
                raiz = (-b + math.sqrt(delta))/(2*a)
                return 1, raiz
            else:
                raiz = (-b + math.sqrt(delta))/(2*a)
                raiz2 = (-b - math.sqrt(delta))/(2*a)
                return 2, raiz, raiz2
     
    def main(self):
        a_digitado = int(input("Insira o 'a' da equação: "))
        b_digitado = int(input("Insira o 'b' da equação: "))
        c_digitado = int(input("Insira o 'c' da equação: "))
        print(self.calcula_raizes(a_digitado,b_digitado,c_digitado))


