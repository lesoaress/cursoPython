opcao = int(input("1 - Mulher \n2 - Homem\n"))
altura = float(input("Informe sua altura:"))

if opcao == 1:
    peso_ideal = (62.1*altura)-44.7
if opcao == 2:
    peso_ideal = (72.7*altura)-58

print("De acordo com o seu sexo e sua altura, seu peso ideal é:", round(peso_ideal, 1))
    
