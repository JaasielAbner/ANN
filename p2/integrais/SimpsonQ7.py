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

x = [0.295, 0.551, 0.807, 0.8655, 0.924, 1.0465, 1.169, 1.1775, 1.186, 1.4845, 1.783, 2.4365, 3.09, 3.1285, 3.167, 3.559, 3.951, 4.1225, 4.294, 4.3725, 4.451]
y = [2.232, 2.863, 2.989, 2.96, 2.916, 2.789, 2.637, 2.626, 2.615, 2.263, 2.047, 2.189, 2.928, 2.956, 2.978, 2.653, 1.383, 1.021, 1.148, 1.391, 1.728]

intervalo = [0.295,4.451]
subintervalos = [4, 18, 32, 60, 98, 108, 132, 152, 194, 212, 278]

'''
n = len(subintervalos)
for i in range(n):
    print(simps(f, intervalo[0], intervalo[1], subintervalos[i]))
'''

simpsPonto(x, y)