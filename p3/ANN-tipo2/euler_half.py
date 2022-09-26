import math

def euler_half(f, x0:float, y0:float, h:float, n:int):
    r = []
    for _ in range (n):
        #realizar as iterações
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2)*m1)
        yk = y0 + h * m2
        #atualizando para próxima iteração
        y0 = yk
        x0 += h
        #colocando valores na lista
        r.append((x0, y0))

    return r

if __name__ == "__main__":
#exemplo
#y'= x+y, y(0)=1
    def f(x, y):
        return y*(2 - x) + x + 1

    x0 = 1.00304
    y0 = 2.61034
    h  = 0.17368
    n  = 10

    r = euler_half(f, x0, y0, h, n)
    print(r)
