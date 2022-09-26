import numpy as np
import math


def best_line(x, y, grau=1):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    # soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a * (x/(x+b))
    # funcaomath.pow(x,b)


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':
    x = [2.0963, 3.6766, 4.5085, 6.1141, 7.9251, 10.2103, 11.8599, 13.6646, 14.5129, 15.8982, 18.1988, 19.5029]
    y = [1.4658, 1.932, 2.1098, 2.353, 2.5586, 2.7493, 2.7718, 2.8557, 2.9061, 2.9541, 3.0289, 3.0492]
    values = [12.085, 13.4581, 17.8903]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = (np.divide(1, y))

    xt = [xi + k2 for xi in x]

    x_ = np.divide(1, x)
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = 1/a0

    b = a1/a0
    print('Coeficientes da reta')
    print(f'{a0 = } e {a1 = }')

    print('Coeficientes')
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px = }')

    # visualização

    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt)

    # plt.savefig('best_poly_regressao_potencia.png')
