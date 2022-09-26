import math
import matplotlib.pyplot as plt
import numpy as np

def euler(f, x0, y0, h, n):
    r = []
    for i in range(n):
        #realizar iteracoes
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        yk = y0 + h * m2

        y0 = yk
        x0 += h
        r.append((x0, y0))
    return r

if __name__ == '__main__':

    # def f(x, y):
    #     return y*(2-x)+x+1

    def f(x, y):
         return k*y + v

    h=0.0625
    n = 1
    k = 0.0237
    v = 95020

    x0, y0 = 0, 1914093

    # a sua função vira aquele k*P
    # k ele te dá 
    # o P é só 'y"
    # x0 é o tempo, y0 é o número de pessoas que ele te dá
    # e n é meio que o "1 ano"
    # se não me engano
    # só tu pegar o último valor dos 16 que brotar e é aquilo lá

    resposta = euler(f, x0, y0, h=0.1922 , n=10)
    print(resposta)

    x, y = zip(*resposta)
    # print(x)
    # print(y)
    # plt.scatter(x,y)
    # plt.savefig('euler_half.png')
