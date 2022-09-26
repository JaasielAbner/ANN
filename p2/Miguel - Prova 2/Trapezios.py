import math

def trapz(f, a, b, n):
    h = (b - a)/n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a) + f(b)
    soma *= h/2
    return soma

# def f(x):
#     return math.exp(-x**2)

# x = [0.178, 0.489, 1.047, 1.172, 1.379, 1.475, 1.915, 1.966, 1.988, 2.219, 2.243, 2.564, 2.61, 3.071, 3.284, 3.647, 4.073, 4.111, 4.244, 4.738, 4.768]
# y = [1.823, 2.757, 2.788, 2.633, 2.376, 2.272, 2.007, 2.001, 2.0, 2.048, 2.059, 2.313, 2.364, 2.912, 2.997, 2.416, 1.085, 1.033, 1.052, 2.937, 2.982]
# soma = 0
# xy = zip(x,y)

# for a2,b2 in zip(x[1:],y[1:]): # lista de x e y removidos os primeiros elementos
#     for a1, b1 in zip(x,y):
#         soma += ((a2-a1) * (b2 + b1))/2
#         x.pop(0) # removendo os primeiros elementos das listas de x e y
#         y.pop(0)
#         break

# print(soma)

def f(x):
    return -x*(x-21)*(x+1)
    
a, b = 0, 12 # extremos do intervalo
n = 31 #nro de pontos na partição
print(trapz(f, a, b, n))
