x = input("Digite um número sem pontuações: ")
tamanho = len(x)
x = int(x)
i  = 0
soma = 0

while i < tamanho:
   num = x % 10
   print(num)
   x = x // 10
   soma = soma + num 
   i+=1

print("Soma entre todos os algarismos: ", soma)
    
