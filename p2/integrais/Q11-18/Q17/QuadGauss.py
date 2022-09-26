import math

def quadratura(f, x, c):
    return sum([ci * f(xi) for ci, xi in zip(c, x)])

def change(f, a, b):
    def g(u):
        return f(a + (b - a) * (u + 1) / 2) * (b - a) / 2
    return g


if __name__ == '__main__':


    #exemplo 1
    x = ([0, -0.7745966692414834, 0.7745966692414834])
    c = ([0.8888888888888888, 0.5555555555555556, 0.5555555555555556])

    def f_1(x):
        return -x*(x-21)*(x+1)

    a = 0
    b = 12

    g = change(f_1, a, b)

    aprox_1 = quadratura(g, x, c)

    print(f'{aprox_1}')