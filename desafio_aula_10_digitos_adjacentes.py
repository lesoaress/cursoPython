numero_str = input("Digite um número: ")

##verifica o tamanho do número
tamanho_do_numero = len(numero_str)

##transforma o número para inteiro
numero = int(numero_str)

##cria um contador de números adjacentes
contador_numeros_adjacentes = 0

##cria um contador para percorrer o tamanho do número
i = 0

penultimo_digito = ((numero // 10)%10)

ultimo_digito =  numero % 10

while i < tamanho_do_numero and contador_numeros_adjacentes < 1:
    if ultimo_digito == penultimo_digito:
        contador_numeros_adjacentes+=1
    numero = numero // 10
    ultimo_digito = penultimo_digito
    if ((numero // 10)%10) == numero:
         penultimo_digito = numero
    else:
        penultimo_digito = ((numero // 10)%10)
    i+=1

if contador_numeros_adjacentes == 1:
    print("O número inserido possui dois algarismos adjacentes")
else:
    print("O número inserido não possui dois algarismos adjacentes")
    
