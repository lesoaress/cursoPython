numero_str = input("Digite um número: ")
tamanho_do_numero = len(numero_str)
print(tamanho_do_numero)
numero = int(numero_str)
contador_numeros_adjacentes = 0
i = 0

while i< tamanho_do_numero:
    numero = numero % 10
    print(numero)
    tamanho_do_numero -= tamanho_do_numero
    
