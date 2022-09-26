""" A taxa de crescimento de uma população P ao longo do tempo t (em anos), com taxa de natalidade constante λ e taxa de imigração constante ν é modelada pela seguinte equação diferencial
dPdt=λP+ν,
Assuma que a população de um país em t=0 seja de 1795811 indivíduos, que a taxa de natalidade seja constante igual a λ=0.0999 e que ν=86225 seja a taxa de imigração anual. Use o método do ponto médio de Euler para estimar o número de indivíduos nessa população após 1 ano. Use tamanho do passo h=0.0625. """

def true_euler(f, k, x0, y0, h, n):
    for i in range(n):
        y0 += h * f(x0, y0, k)
        x0 += h        
        #print(f'x_{i + 1}={x0} e y_{i+1}={y0}')
    print(f'{y0}')

def euler_mid(f, k, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0, k)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1, k)
        y0 = y0 + h * m2
        x0 += h
        yield x0, y0

if __name__ == '__main__':
    def f(x, y, k):
        return k*y + 86225  # valor de v
    
    x0, y0 = 0.0, 1795811 # x0 = t, y0 = individuos
    h = 0.0625
    k = 0.0999 # gama
    n = int(1 / h)
    #true_euler(f, k, x0, y0, h, n)

    r2 = euler_mid(f, k, x0, y0, h, n)
    x2, y2 = zip(*r2)
    print(y2)