""" Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.325 e y0=0.606. Use o método de Ralston para estimar o valor da solução exata desse PVI nos pontos
x1=0.626, x2=0.871, x3=1.125, x4=1.273, x5=1.643, x6=1.784, x7=2.203, x8=2.453, x9=2.539 e x10=2.886. """

def ralston_h_variavel(f, x0, y0, n,b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
     vals = []
     for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + 3/4 *h, y0 + m1 *3/4 * h )
        y0 += (1 *m1 + m2*2)*h/3
        x0 += h
        vals.append([x0, y0])
     return vals

#Q10 Prova:
def f(x,y):
    return y*(2-x)+x+1

n = 10
b = 2/3
x_values = [0.626, 0.871, 1.125, 1.273, 1.643, 1.784, 2.203, 2.453, 2.539, 2.886]

x0, y0 = 0.325, 0.606

e = ralston_h_variavel(f,x0,y0,n, b, x_values)
for xi, yi in e:
    print(xi, yi)