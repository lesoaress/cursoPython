def le_strings():
    strings = []
    i = 0
    qtde_strings = int(input("Digite a quantidade de strings: "))
    while i < qtde_strings:
        string = input("Digite a string número "+ str(i)+ ": ")
        strings.append(strings)
        i += 1
    return menor_string(strings)
    
def menor_string(strings):
    menor_string = strings[0].lower()
    i = 1
    tamanho_da_lista = len(strings)

    while i < tamanho_da_lista:
        strings[i] = strings[i].lower()
        if strings[i] < menor_string:
            menor_string = strings[i]
        i += 1

    return menor_string
        
def teste_pontual(strings, esperado):
    retorno_funcao = menor_string(strings)
    if retorno_funcao != esperado:
        print("Não deu certo!!!! \nValor esperado: ", esperado, "\nRetorno função: ", retorno_funcao)
    else:
        print("deu certo!!!! \nValor esperado: ", esperado, "\nRetorno função: ", retorno_funcao)

def testa_menor_string():
    teste_pontual(["ana", "maria", "José", "Valdemar"], "ana")
    
