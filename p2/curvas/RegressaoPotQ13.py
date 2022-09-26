import numpy as np

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi**p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi*xi**i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a*x**b


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':
    x = [0.563, 0.82, 0.9538, 1.2327, 1.3838, 1.6427, 1.9375, 2.1481, 2.3183, 2.5147, 2.7057, 2.913]
    y = [0.0204, 1.7682, 1.9178, 4.0736, 8.8372, 13.4137, 19.4624, 26.4325, 34.0715, 43.9046, 55.0945, 69.065]
    values = [1.3033, 1.3394, 2.7018]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(yt)

    xt = [xi + k2 for xi in x]

    x_ = np.log(xt)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    a = np.exp(a0)

    b = a1

    print('Coeficientes da reta')
    print(f'{a0} e {a1}')

    print('Coeficientes da potencia')
    print(f'{a } e {b}')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    for value in values:
        print(q(value))

"""     # visualização

    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt)

    plt.savefig('best_poly_regressao_potencia.png') """
