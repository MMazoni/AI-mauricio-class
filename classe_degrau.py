# -*- coding: utf-8 -*-

class Degrau:


    def __init__(self, weight1, weight2, limiar):
        self.weight1 = weight1
        self.weight2 = weight2
        self.limiar = limiar


    def degrau(self, x1, x2):
        y1 = self.calcula_ativacao(x1, x2, self.weight1, self.weight2)
        if y1 > self.limiar:
            y = 1
        else:
            y = 0
        return y
        
        
    def calcula_ativacao(self,x1, x2, peso1, peso2):
        return x1 * peso1 + x2 * peso2 # bias


