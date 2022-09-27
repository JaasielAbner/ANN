# uma função qualquer
from math import exp


def f(x):
    return 3386768 - (1578929 * exp(x) + 489875/x * (exp(x) - 1))

n = 7
x0, x1 = [0.1, 1.39]
itr = {}
itr[0] = x0
itr[1] = x1

a, b = x0, x1
for i in range(n):
    try:
        xn = (a * f(b) - b * f(a)) / (f(b) - f(a)) # a - f(a) / ((f(b) - f(a))/ (b - a))
    except:
        raise ValueError(f"Divisão por zero para {a}, {b} na iteração {i}")
    itr[i + 2] = xn
    a, b = b, xn

for k, v in itr.items():
    print(k, v)

