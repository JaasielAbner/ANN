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
    return (9 + 4*(math.cos(0.49*x)**2))*(5*math.exp(-0.52*x) + 2*math.exp(0.18*x))

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'Area = {somas}')

x = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5, 8.25, 9.0, 9.75, 10.5, 11.25, 12.0]
y = [9.95,9.5,9.13,8.72,8.09,7.65,7.4,6.97,6.47,6.1,5.74,5.21,5.0,4.55,4.15,3.47,3.12]

a = 2.74
b = 7.69
n = 19

#trapz(f, a, b, n)
trapzPonto(x, y)