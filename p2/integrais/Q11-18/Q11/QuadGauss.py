import math

def quadratura(f, x, c):
    return sum([ci * f(xi) for ci, xi in zip(c, x)])

def change(f, a, b):
    def g(u):
        return f(a + (b - a) * (u + 1) / 2) * (b - a) / 2
    return g

if __name__ == '__main__':

    #exemplo 1
    x = ([0, -0.5384693101056831, 0.5384693101056831, -0.906179845938664, 0.906179845938664])
    c = ([0.5688888888888889, 0.47862867049936647, 0.47862867049936647, 0.23692688505618908, 0.23692688505618908])

    def f_1(x):
        g = 9.81
        m = 65.93
        cd = 0.21
        return math.sqrt((g*m) / cd) * math.tanh(math.sqrt((g*cd) / m) * x)

    a = 0
    b = 5.59

    g = change(f_1, a, b)

    aprox_1 = quadratura(g, x, c)

    print(f'{aprox_1}')