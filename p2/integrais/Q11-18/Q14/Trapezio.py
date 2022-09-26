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


x = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0]
y = [229.54, 170.02, 252.24, 105.1, 200.25, 134.73, 288.98]

_x = []
m = len(x)
for xi in range(m):
  _x.append(x[xi]/3600)

a = 2.74
b = 7.69
n = 19

#trapz(f, a, b, n)
trapzPonto(_x, y)