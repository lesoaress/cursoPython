import math
metros_quadrados = float(input("Informe o tamanho da área em metros quadrados: "))
 
litros = metros_quadrados / 3

qtde_latas = math.ceil(litros/18)

total = qtde_latas * 80.0

print("Você irá precisar de", qtde_latas, "latas e custará R$", total)

