# uma função qualquer
from math import exp


def f(x):
    return 3386768 - (1578929 * exp(x) + 489875/x * (exp(x) - 1))

# derivada de f
def df(x):
    return -1578929 * exp(x) + (489875 * (-1 + exp(x)))/x**2 - (489875 * exp(x))/x

x0 = 1.54
n = 6
itr = {}
itr[0] = x0
for i in range(1, n):
    itr[i] = x0 - f(x0) / df(x0)
    x0 = itr[i]

for k, v in itr.items():
    print(k, v, abs(v - 1.7392201937014509))
