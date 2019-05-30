def fatorial(numero):
    fatorial = 1
    while numero > 0:
        fatorial = fatorial *numero
        numero = numero - 1
    print(fatorial)
    
qtde_numeros = 1

while qtde_numeros <=5:
    numero = int(input("Digite um número: "))
    fatorial(numero)
    qtde_numeros +=1
    
