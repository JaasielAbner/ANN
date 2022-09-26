import matplotlib.pyplot as plt
import numpy as np

#   INTERPOLACAO
#           MÉTODOS DAS DIFERENÇAS DIVIDIDAS (de Newton)

# x = [1, 2, 3, 4, 4.2, 4.7, 9, 20]
# y = [2, 5, 1, 3, 1, 2, 10, -3]


def diferenca_div(x, y):
  y = [i for i in y]
  n = len(y)
  coeficientes = [ y[0]] + [0] * (n - 1)
  for i in range(n-1):
    for j in range(n - 1 - i):
      numerador   = y[j+1] - y[j]
      denominador = x[j+1+i] - x[j]
      y[j] = numerador / denominador
    coeficientes[i+1] = y[0]
  return coeficientes

def eq(x, coeficiente):
  n = len(x)
  equacao = ''
  for i in range(n):
    sign = ''
    if i != 0:
      sign = '*'
    equacao += f'{coeficiente[i]:+}{sign}' + '*'.join( [f'(x{-xj:+})' for j, xj in enumerate(x) if j < i] )
  return equacao

#P2.2
y = [1.8099749372185823, 2.6866480011948664, 2.9086969688012188, 2.496042790430524, 1.2995519585320157, 0.08740210414263955, 0.11144330455286494]
x = [-0.402, -0.172, 0.282, 0.457, 0.765, 1.124, 1.247]

if __name__ == "__main__":
  coeficiente = diferenca_div(x,y)
  print("\n",coeficiente,"\n")
  polinomio = eq(x,coeficiente)
  print(polinomio)

  t = np.linspace(min(x), max(x), 100)
  def p(x):
    return eval(polinomio)
  plt.plot(t, p(t))
  plt.scatter(x, y, zorder=10)
  plt.savefig("diff-div.png")
