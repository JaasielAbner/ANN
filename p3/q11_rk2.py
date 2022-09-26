import math
import matplotlib.pyplot as plt
import numpy as np

# exemplo y'= 1 +xy, y(1) = 2

def RK2(f, x0, y0, h, n, b=0.821):
    a = 1 - b
    p = 1 / (2 * b)
    q = p
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0+p*h, y0+q*h*m1)
        y0 += (a * m1 + b * m2) * h
        x0 += h
        yield [x0,y0]



def f(x,y):
    return - (y/math.sqrt((afunc**2) - (y**2)))
afunc = 9.892
x0, y0 = 1.061, 4.289
e = RK2(f,x0,y0, h=0.234,n=10)
for xi, yi in e:
    print(xi, yi)
