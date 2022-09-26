import math

def euler(f, x0, y0, h, n):
    for i in range(n):
        y0 += f(x0, y0) * h
        x0 += h
        print(f'x_{i+1}= {x0}, y_{i+1} = {y0}')


#Q7 Prova:
def f(x, y):
    return y*(1-x)+x+2

x0, y0 = 0.96329,0.91277
h = 0.13123
n = 10

euler(f,x0,y0,h,n)