def primo(x):
    fator = 2
    if x == 2:
        return True
    while x % fator != 0 and fator <= x/2:
        fator += 1
    if x % fator == 0:
        return False
    else:
        return True
    
n = int(input("Informe um número inteiro positivo: "))

while n > 0:
    if primo(n):
        print(True)
    else:
        print(False)
    n = int(input("Informe um número inteiro positivo: "))
    

        
        
        

 
