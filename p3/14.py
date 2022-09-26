import numpy as np


def rk4(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2)*m1)
        m3 = f(x0 + h/2, y0 + (h/2)*m2)
        m4 = f(x0 + h, y0 + h*m3)
        yk = y0 + h*(m1 + 2*m2 + 2*m3 + m4)/6
        x0 += h
        y0 = yk
        vals.append([x0, y0])
    return vals


def f(x, y):
    return y*(1 - x) + x + 2


def rebeldes(t, pt):
    lambda_ = 0.02945
    r = 0.11952

    return r*lambda_*(1-pt)


def rebeldes_exact(t):
    a = 0.00165  # a = p0
    l = 0.02945  # lambda
    r = 0.11952
    return np.exp(-l*r*t)*(-1 + a + np.exp(l*r*t))
    # return 1 - 0.99382*np.exp(-0.00352888*t)


def diff(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))


if __name__ == '__main__':
    x0, y0 = 0, 0.00165 
    h = 1
    n = 150

    r = rk4(rebeldes, x0, y0, h, n)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*r)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')
        print(f'{abs(rebeldes_exact(i) - yi)},', end='')
        # print(f'{rebeldes_exact(xi)},', end='')