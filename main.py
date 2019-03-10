from classe_degrau import Degrau


if __name__ == '__main__':
    w1 = 1
    w2 = 1
    limiar = 1.5
    x1 = [0, 0, 1, 1]
    x2 = [0, 1, 0, 1]
    ld = Degrau(w1, w2, limiar)
    for i in range(4):
        y = ld.degrau(x1[i], x2[i])
        print("porta E: F = (x1 = {}) E (x2 = {}) = {}".format(x1[i],x2[i],y))
