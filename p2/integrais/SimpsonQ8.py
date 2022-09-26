import math

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))

def f(x):
    return math.sqrt(1 + math.cos(x)**2)

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')

x = [0.068, 0.0825, 0.097, 0.172, 0.247, 0.314, 0.381, 0.51, 0.639, 0.658, 0.677, 0.7435, 0.81, 0.951, 1.092, 1.249, 1.406, 1.4965, 1.587, 1.6735, 1.76, 2.06, 2.36, 2.5105, 2.661, 2.7285, 2.796, 3.0685, 3.341, 3.347, 3.353, 3.4665, 3.58, 3.751, 3.922, 4.024, 4.126, 4.1825, 4.239, 4.3875, 4.536, 4.564, 4.592, 4.727, 4.862]
y = [1.443, 1.49, 1.538, 1.801, 2.069, 2.295, 2.497, 2.797, 2.961, 2.974, 2.984, 3.0, 2.988, 2.891, 2.734, 2.535, 2.346, 2.251, 2.17, 2.106, 2.058, 2.004, 2.129, 2.258, 2.423, 2.506, 2.592, 2.909, 2.974, 2.97, 2.966, 2.837, 2.601, 2.076, 1.475, 1.184, 1.018, 1.001, 1.045, 1.449, 2.148, 2.287, 2.422, 2.914, 2.944]

intervalo = [-1.091, 1.438]
subintervalos = [4, 18, 32, 60, 98, 108, 132, 152, 194, 212, 278]

'''
n = len(subintervalos)
for i in range(n):
    print(simps(f, intervalo[0], intervalo[1], subintervalos[i]))
'''

simpsPonto(x, y)