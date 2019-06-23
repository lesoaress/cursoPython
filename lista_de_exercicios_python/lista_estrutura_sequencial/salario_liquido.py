valor_hora = float(input("Informe quanto você ganha por hora: "))
horas_mes = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_mes
INSS = salario_bruto*0.08
imposto_de_renda = salario_bruto*0.11
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - (INSS + sindicato + imposto_de_renda)

print("Salário Bruto: R$", salario_bruto)
print("INSS: R$", INSS)
print("Sindicato: R$", sindicato)
print("Salário Líquido: R$", salario_liquido)
print("Salário Bruto: R$", salario_bruto, "\n- IR: R$", imposto_de_renda, "\n- INSS: R$", INSS, "\n- Sindicato: R$", sindicato, "\n= Salário Líquido: R$", salario_liquido)
