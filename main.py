from classe_degrau import Degrau


if __name__ == '__main__':
    w1 = 1
    w2 = 1
    limiar = 1.5
    x1 = [0, 0, 1, 1]
    x2 = [0, 1, 0, 1]
    ld = Degrau(w1, w2, limiar, x1, x2)
    for i in range(4):
        y = ld.verifica_degrau(x1[i], x2[i], ld.weight1, ld.weight2)
        print("porta E: F = (x1 = {}) E (x2 = {}) = {}".format(ld.x1[i],ld.x2[i],y))
