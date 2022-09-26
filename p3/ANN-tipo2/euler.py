import math
def euler(f, x0:float, y0:float, h:float, n:int):
    for k in range(n):
        #uma aproximação para phi(xk)
        y = y0 + h *f(x0 + k*h, y0)
        print(f'x_{k+1} = {x0 + (k+1)*h}\ny_{k+1} = {y}\n')
        y0 = y

#exemplo

x0 = 0.40314
y0 = 0.32935
h  = 0.18267
n  = 10
# y'=x+y, y(0)=1
def f(x,y):
    return y*(2 - x) + x + 1

euler(f, x0, y0, h, n)
