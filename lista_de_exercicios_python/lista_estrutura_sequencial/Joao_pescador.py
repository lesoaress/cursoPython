peso = float(input("Informe a quantidade de peso de peixes pescados: "))

excesso = peso - 50

if excesso > 0:
    multa = excesso * 4.0
    print("Você excedeu o peso permitido! A multa será de:", multa, "reais!")
else:
    print("Você não excedeu o peso permitido!")
