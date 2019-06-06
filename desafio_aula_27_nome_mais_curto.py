def le_nomes():
    nomes = []
    i = 0
    qtde_nomes = int(input("Digite a quantidade de nomes: "))
    while i < qtde_nomes:
        nome = input("Digite o nome número "+ str(i)+ ": ")
        nomes.append(nome)
        i += 1
    return mais_curto(nomes)

def mais_curto(nomes):
    i = 1
    nomes[0] = nomes[0].strip()
    tamanho_do_menor_nome = len(nomes[0])
    menor_nome = nomes[0]

    while i < len(nomes):
        nomes[i] = nomes[i].strip()
        if len(nomes[i]) < tamanho_do_menor_nome:
            tamanho_do_menor_nome = len(nomes[i])
            menor_nome = nomes[i]
        i += 1
    return menor_nome

def teste_pontual(nomes, esperado):
    valor_funcao = mais_curto(nomes)
    if valor_funcao != esperado:
        print("Não deu certo!!!! A função retornou: ", valor_funcao)
    else:
        print("Deu certo!!!!! \nValor esperado: ", esperado, "\nA função retornou: ", valor_funcao)
        
def testa_mais_curto():
    teste_pontual(["joao", "    ana", "joaquina"], "ana")
    teste_pontual(["      let", "    a", "oi"], "a")

    
    

        
    
    
