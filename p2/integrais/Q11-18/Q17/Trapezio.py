import math

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a)
    soma += f(b)
    soma *= (h/2.0)
    print(f'Area aproximadamente: {soma}')

def f(x):
    return -x*(x-21)*(x+1)

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'Area = {somas}')



x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
y = [0, 102, 230, 359, 506, 670, 818, 965, 1088, 1203, 1325, 1466, 1630, 1826, 2046, 2316, 2594, 2901, 3201]

a = 0
b = 12
n = 31

trapz(f, a, b, n)
#trapzPonto(_x, y)