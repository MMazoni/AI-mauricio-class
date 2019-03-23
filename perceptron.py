class Perceptron:

    f = None
    def __init__(self, w, x0, x1, limiar, y0, y1, taxa_aprendizado):
        self.w = w
        self.x0 = x0
        self.x1 = x1
        self.limiar = limiar
        self.y0 = y0
        self.y1 = y1
        self.taxa_aprendizado = taxa_aprendizado

    def entrada0(self, weight):
        print("Entrada 0 ")
        self.w = weight
        u0 = 0
        for i in range(len(x0)):
            u0 += x0[i]*weight[i][0]
            # print("x0[{}] = {}".format(i, x0[i]))
            # print("w[{}] = {}".format(i, w[i]))
        print("u0 = {}".format(u0))
        if u0 > limiar:
            Perceptron.f = 1
        else:
            Perceptron.f = 0
        for i in range(len(x0)):
            weight[i][0] = weight[i][0] + taxa_aprendizado*(y0-Perceptron.f)*x0[i]
            # print("pesos w = \t", w[i][0])
        return weight

    
    def entrada1(self, weight):
        print("Entrada 1 ")
        self.w = weight
        u0 = 0
        for i in range(len(x1)):
            u0 += x1[i]*weight[i][0]
        print("u0 = {}".format(u0))
        if u0 > limiar:
            Perceptron.f = 1
        else:
            Perceptron.f = 0
        for i in range(len(x1)):
            weight[i][0] = weight[i][0] + taxa_aprendizado*(y1-Perceptron.f)*x1[i]
            # print("pesos w =" w[i][0])
        return weight

    def iteracao(self):
        n = 0
        while n < 5:
            self.w = self.entrada0(w)
            for i in range(len(w)):
                print("Pesos w = {}".format(w[i][0]))
            print("Valor de f = {}".format(Perceptron.f))
            
            self.w = self.entrada1(w)
            for i in range(len(w)):
                print("Pesos w = {}".format(w[i][0]))
            print("Valor de f = {}".format(Perceptron.f))
            
            n += 1
            print("Numero de treinamentos {}".format(n))
            print('\n')


    def testa_rede(self, weight, x0, x1):
        print("TESTE DE REDE NEURAL")
        self.w = weight
        x0 = self.x0
        x1 = self.x1

        for i in range(len(weight)):
            print("pesos resultantes do treinamento ")
            print("w[0][0] = {}".format(weight[i][0]))
        print("\n")    
        u0 = 0
        for i in range(len(x0)):
            u0 += x0[i]*weight[i][0]
        if u0 > limiar:
            Perceptron.f = 1
        else:
            Perceptron.f = 0
        print("u0 = {}".format(u0))
        print("teste da entrada x0 saida y = {}".format(Perceptron.f))

        u0 = 0
        for i in range(len(x1)):
            u0 += x1[i]*weight[i][0]
        if u0 > limiar:
            Perceptron.f = 1
        else:
            Perceptron.f = 0
        print("u0 = {}".format(u0))
        print("teste da entrada x1 saida y = {}".format(Perceptron.f))


if __name__ == '__main__':
    w = [[-0.5441],[0.5562],[-0.4074]]
    x0 = [-1, 2, 2]
    x1 = [-1, 4, 4]
    # x[0] = x1[0] = -1 = entrada do bias
    # x[0][0] = -0.5441 = peso do bias
    limiar = 0
    y0 = 1
    y1 = 0
    taxa_aprendizado = 0.1
    p = Perceptron(w, x0, x1, limiar, y0, y1, taxa_aprendizado)
    p.iteracao()
    p.testa_rede(p.w, p.x0, p.x1)

    