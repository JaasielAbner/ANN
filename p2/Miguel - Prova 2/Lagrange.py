import math

def lagrange(x,y):
    # retorna a equação do polinômio de lagrange
    # coordenadas x e y dos pontos que definem o polinomio
    if (len(x) != len(y)):
        raise TypeError("O número de coordenas x e y são diferentes")
    
    equacao = ''
    n = len(x)
    for k in range(n):
        numerador = '*'.join([f'(x{-xi:+})' for i, xi in enumerate(x) if i != k]) # numerador da função L_k
        #                    ^^^^^^^^^^^^^
        #                          /\
        # Não sei que porra é essa ||

        denominador = '*'.join([f'({x[k]}{-xi:+})' for i, xi in enumerate(x) if i != k]) # denominador da função L_k
        #                      ^^^^^^^^^^^^^^^^^^
        #                             /\
        # Isso aqui menos ainda       ||

        equacao += f'{y[k]:+}*({numerador})/({denominador})'
    return equacao

if __name__ == '__main__':
    def f(x):
        return math.sin(x)**4 - 4*(math.sin(x))**2 + math.cos(x**2) + math.log((-x)**2)+5

    x = [1.551, 1.802, 2.111, 2.548, 2.931, 3.311, 3.553, 3.844, 4.163, 4.549, 4.751]  # coordenadas x dos pontos
    y = [f(xi) for xi in x] # coordenadas y dos pontos
    equacao = lagrange(x,y)

    def p(x):
        return eval(equacao)

    # print(x2)
    # print(y2)

    # gráficos

    # from matplotlib import pyplot as plt
    # import numpy as np

    # t = np.linspace(-1,1,200)
    
    # plt.plot(t, subs(t), label='interpolador')
    # plt.plot(t, f(t), label='função')

    # plt.scatter(x2,y2)
    # plt.savefig('lagrange.png')
