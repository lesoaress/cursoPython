def main():
    carro1 = Carro('brasília', 1968, 'amarelo', 80)
    carro2 = Carro('fuscão', 1981, 'preto', 95)

    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(800)
    carro1.pare()
    carro2.acelere(100)

class Carro:
    def __init__(self, modelo, ano, cor, velocidade_maxima):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade_maxima = velocidade_maxima
        self.velocidade = 0

    def imprima(self):
        if self.velocidade == 0:
            print("%s %s %d"%(self.modelo, self.cor, self.ano))
        elif self.velocidade < self.velocidade_maxima:
            print("%s %s indo a %d Km/h"%(self.modelo, self.cor, self.velocidade))
        else:
            print("%s %s indo muito rápido!"%(self.modelo, self.cor)) 

    def acelere(self, velocidade):
        self.velocidade = velocidade
        if self.velocidade > self.velocidade_maxima:
            self.velocidade = self.velocidade_maxima
        self.imprima()

    def pare(self):
        self.velocidade = 0
        self.imprima()

main()
