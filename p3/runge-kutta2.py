import math
import matplotlib.pyplot as plt
import numpy as np

# exemplo y'= 1 +xy, y(1) = 2
'''
Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.126 e y0=1.922. Use o método de Runge-Kutta de ordem 2 com b=0.689 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,10. Use h=0.132.
'''

def RK2(f, x0, y0, h, n, b=0.599):
    a = 1 - b
    p = 1 / (2 * b)
    q = p
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0+p*h, y0+q*h*m1)
        y0 += (a * m1 + b * m2) * h
        x0 += h
        yield [x0,y0]


#Q11 Prova:
def f(x,y):
    return y*(1-x)+x+2

x0, y0 = 0.841, 0.771
e = RK2(f,x0,y0, h=0.188,n=10)
for xi, yi in e:
    print(xi, yi)
