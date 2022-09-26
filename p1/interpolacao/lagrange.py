import math
from typing import Type
import matplotlib.pyplot as plt
import numpy as np




#   INTERPOLACAO
#           METODO DE LAGRANGE


def lagrange(x,y):
  # retornar a equacao do polinomio de lagrange
  n = len(x)
  if n == len(y):
    eq = ''
    for k in range(n):
      numer = '*'.join([f'(x{-xi:+})' for i, xi in enumerate(x) if i != k])
      denom = '*'.join([f'({x[k]}{-xi:+})' for i, xi in enumerate(x) if i != k])
      eq += f'{y[k]:+}*({numer})/({denom})'
    return eq
  else:
    raise TypeError("O numero de coordenadas de x != de numero de coordenadas de y\n")


def subs(x):
  #retornar o valor do polinomio de lagrange em um ponto X
  return eval(eq)

x = [-1.65722, 1.95035]
y = [1.8239941579105157, 3.0152687386168737]
if __name__ == "__main__":

  eq = lagrange(x,y)
  def subs(x):
    return eval(eq)

  print("p(x) = ", eq)
  #print(subs(1), subs(2), subs(3))

  t = np.linspace(min(x),max(x),100)
  plt.plot(t, subs(t))
  plt.scatter(x,y)
  plt.savefig("./lagrange.png")

