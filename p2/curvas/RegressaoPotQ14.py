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
    #soma das coordenadas x*y
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
    x = [1.4963, 3.3128, 5.3527, 5.7798, 7.944, 10.4917, 11.1963, 12.1685, 14.2535, 16.2032, 17.1481, 19.591]
    y = [0.9014, 1.5269, 1.8566, 1.9497, 2.2128, 2.3146, 2.3155, 2.3726, 2.4194, 2.4866, 2.5061, 2.5538]
    values = [6.5873, 11.8104, 13.7054]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = (np.divide(1,y))

    xt = [xi + k2 for xi in x]

    x_ = np.divide(1,x)
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = 1/a0

    b = a1/a0
    print('Coeficientes da reta')
    print(f'{a0 } e {a1 }')

    print('Coeficientes')
    print(f'{a } e {b }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px}')

"""# visualização

    import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt)

    plt.savefig('best_poly_regressao_potencia.png') """
