# posição pode ser mais lento que o método da bisseção

# uma função qualquer
from math import exp


def f(x):
    return 3386768 - (1578929 * exp(x) + 489875/x * (exp(x) - 1))

n = 12
a, b = [0.1,1.8]
for i in range(n):
    xn = (a * f(b) - b * f(a)) / (f(b) - f(a))
    if f(xn) == 0:
        print('A raiz é:', xn)
    elif f(a) * f(xn) < 0:
        b = xn
    else:
        a = xn
    print(i, xn, abs(xn - 1.7392201937014509))
