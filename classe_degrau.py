# -*- coding: utf-8 -*-

class Degrau:

    def __init__(self, weight1, weight2, limiar, x1, x2):
        self.weight1 = weight1
        self.weight2 = weight2
        self.limiar = limiar
        self.x1 = x1
        self.x2 = x2


    def degrau(self):
        n = 0
        while True:
            for i in range(4):
                y1 = calcula_ativacao(self.x1[i], self.x2[i], self.weight1, self.weight2)
            if y1 > self.limiar:
                y = 1
            else:
                y = 0
            break

    def calcula_ativacao(x1, x2, peso1, peso2):
        return x1 * peso1 + x2 * peso2 # bias

    def verifica_degrau(self, x1, x2, peso1, peso2):
        saida = x1 * peso1 + x2 * peso2
        if saida > self.limiar:
            y = 1
        else:
            y = 0
        return y
