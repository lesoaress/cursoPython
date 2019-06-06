def min_max(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "Cº")
    print("A maior temperatura do mês foi: ", maxima(temperaturas), "Cº")

def minima(temperaturas):
    min = temperaturas[0]
    i = 0
    while i < len(temperaturas):
        if temperaturas[i] < min:
            min = temperaturas[i]
        i += 1
    return min

def maxima(temperaturas):
    max = temperaturas[0]
    i = 0
    while i < len(temperaturas):
        if temperaturas[i] > max:
            max = temperaturas[i]
        i += 1
    return max

def teste_pontual(temp, valor_esperado, min_ou_max):
    if min_ou_max == "min":
        valor_calculado = minima(temp)

    if min_ou_max == "max":
        valor_calculado = maxima(temp)
    
    if valor_calculado != valor_esperado:
        print("Valor errado para array ", temp)
        print("Valor esperado = ", valor_esperado)
        print("Valor calculado = ", valor_calculado)

def testa_minima_e_maxima():
    print("Inciando os testes...")
    
    i = 0
    temperaturas = [[0], [0, 0, 0, 0, 0], [30, 27, 44, 5, 7, 2], [-1, -15, -12, 0, 20, 30]]
    esperados_minimas = [0, 0, 2, -15]
    esperados_maximas = [0, 0, 10, 44, 30]
    
    print("Testes temperaturas mínimas; ")

    while i < len(temperaturas):
        teste_pontual(temperaturas[i], esperados_minimas[i], "min")
        i += 1
    
    print("Testes temperaturas máximas: ")
    while i < len(temperaturas):
        teste_pontual(temperaturas[i], esperados_maximas[i], "max")
        i += 1
    
    print("Finalizando os testes...")
