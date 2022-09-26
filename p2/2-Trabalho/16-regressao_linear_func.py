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
    return (a*x**2)/(b+x**2)
    # funcaomath.pow(x,b)


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':
    x = [1.2678, 2.3802, 3.2611, 4.3268, 5.1626, 5.6998, 6.9716, 7.5496, 9.2293, 9.2912, 10.3551, 11.7861]
    y = [1.9181, 3.3851, 3.979, 4.2291, 4.4209, 4.5244, 4.6034, 4.615, 4.6893, 4.6898, 4.6905, 4.7592]
    values = [2.9056, 6.2089, 6.5603]

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

    x_ = np.divide(1, (np.power(x, 2)))
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = 1/a0

    b = a1*a
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

    plt.savefig('best_poly_regressao_potencia.png')
