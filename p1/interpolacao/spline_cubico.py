import matplotlib.pyplot as plt
import numpy as np

#   INTERPOLACAO
#           MÉTODOS DO SPLINE CÚBICO NATURAL
tmp = []
def spline(x, y):
  """
  Retorna todos os coeficientes de todos os polinômios ak,bk,ck,dk
  """
  n = len(x)
  a = {k: v for k,v in enumerate(y)}
  h = {k: x[k+1] - x[k] for k in range (n - 1)}

  A = [ [1] + [0] * (n - 1) ]
  for i in range(1, n-1):
    linha       = [0] * n           #len(x)
    linha[i-1]  = h[i-1]
    linha[i]    = 2*(h[i-1] + h[i])
    linha[i+1]  = h[i]
    A.append(linha)
  A.append([0] * (n - 1) + [1])

  B = [0]
  for k in range(1, n-1):
    linha = 3 * (a[k+1] - a[k]) / h[k] - 3 * (a[k] - a[k-1]) / h[k-1]
    B.append(linha)
  B.append(0)

  c = dict(zip(range(n), np.linalg.solve(A,B)) )

  b = {}
  d = {}
  for k in range(n - 1):
    b[k] = (1 / h[k]) * (a[k + 1] - a[k]) - (h[k] / 3) * (2*c[k] + c[k + 1])
    d[k] = (c[k + 1] - c[k]) / (3*h[k])

  s = {}
  for k in range(n-1):
    eq = f'{a[k]}{b[k]:+}*(x-{x[k]}){c[k]:+}*(x-{x[k]})**2{d[k]:+}*(x-{x[k]})**3'
    s[k] = {'eq': eq, 'domain': [x[k], x[k+1]]}
    print('\n{}::: ({},{},{},{})\n'.format(k,a[k],b[k],c[k],d[k]))
    tmp.append([a[k],b[k],c[k],d[k]])

  return s

x = [1.961, 2.844, 3.446, 4.41]
y = [-0.8741380, 0.7333098, -0.0291707, 0.9251709]

if __name__ == "__main__":
  eqs = spline(x,y)
  # for i in range(len(tmp)):
  #   print(i,tmp[i])
  print(eqs)
  for key,value in eqs.items():
    def p(x):
      return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
  plt.scatter(x, y)
  plt.legend()
  plt.savefig("spline.png")
