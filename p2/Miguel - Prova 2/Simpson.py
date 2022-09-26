# requer número impar de pontos
import math

def simps(f, a, b, n):
    h = (b - a) / n
    soma_impar = sum([f(a + k * h) for k in range(1, n , 2)])
    soma_par   = sum([f(a + k * h) for k in range(2, n , 2)])
    return (h/3) * (f(a) + 4 * soma_impar + 2 * soma_par + f(b))

def f(x):
    return math.exp(-x**2)

a, b = 0, 1
n = 10 # nro de subintervalos, n/2 é o nro de parabolas, n+1 é o nro de pontos na partição
i1 = simps(f, a, b, n)
print(i1)

# def g(x):
#     return math.cos(x ** 2)

# x = [0.045, 1.968, 3.891, 4.2975, 4.704, 4.706, 4.708, 4.7885, 4.869]
# y = [1.371, 2.001, 1.579, 1.156, 2.856, 2.862, 2.867, 2.997, 2.93]
# soma = 0
# xy = zip(x,y)

# for n in range(2,len(x),2): # lista de x e y removidos os primeiros elementos
#     # print(n, x[n-2], x[n-1], x[n])
#     soma += ((x[n-1] - x[n-2])/3) * (y[n-2] + 4*y[n-1] + y[n])

# print(soma)