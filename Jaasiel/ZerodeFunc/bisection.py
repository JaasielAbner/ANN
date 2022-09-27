# uma função qualquer
from math import exp


def f(x):
    return 3386768 - (1578929 * exp(x) + 489875/x * (exp(x) - 1))

# método da bisseção
a, b = [0.1, 1.58]
n = 12 # número de iterações
for i in range(n):
    m = (a + b) / 2
    if f(m) == 0:
        print('A raiz é:', m)
    elif f(a) * f(m) < 0: # teorema de Bolzano
        b = m
    else:
        a = m
    print(m)
