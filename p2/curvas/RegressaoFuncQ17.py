from re import A
import numpy as np

#BEST_EXP

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p=i+j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a*x*np.exp(b*x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


def modelo(x):
    a, b = -40, -30
    erro = a + (b - a) * np.random.random()
    return 2.5 * np.e ** (1.47 * x) + erro

if __name__ == '__main__':

    x = [1.7161, 2.005, 2.6888, 3.3378, 4.1518, 4.7863, 5.5932, 6.6441, 7.0968, 7.9438, 8.8732, 9.7842]
    y = [5.5409, 5.8808, 6.6495, 7.2118, 7.7975, 8.2362, 8.6234, 9.0605, 9.3909, 9.5398, 9.8288, 10.1551]
    values = [3.9043, 8.5672, 9.1063]

    #transladar os pontos para cima
    k = abs(min(y)) + 1
    yt = [yi + k for yi in y]

    x_ = np.log(x)

    y_ = y

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    print(f'{a0} e {a1}')

    a = a1
    b = a0

    print(f'{a} e {b}')

    n = len(values)
    somas = []
    for xi in range(n):
        print(f'y(x{xi+1}) = {a0+a1*np.log(values[xi])}')

    p = build_func(a, b)

    def q(x):
        return p(x) - k


"""import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt, color='r')
    plt.savefig('best_exp.png') """