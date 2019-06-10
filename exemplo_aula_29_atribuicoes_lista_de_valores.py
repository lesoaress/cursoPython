def peso_altura():
    return 77, 1.83

def pagamento_semanal(valor_por_hora, num_horas = 40):
    assert valor_por_hora >= 0 and num_horas > 0
    return valor_por_hora * num_horas
