import math

#   ZERO DE FUNCAO
#           METODO DO PONTO FIXO
# Entrada: aproximacao inicial (x), funcao (f), erro (err) e numero de iteracoes (numIteracao)

def f(x):
  func = x/2+1/x
  return func


def metodoPontoFixo(x, f, err, numIteracao):
  for i in range(numIteracao):
    x1 = f(x)
    print("x_{} = {}\n".format(i+1,x1))
    if x1 < err:
      break
    x = x1


x0 = 1.1683
iterations = [1, 2, 3, 4, 5, 6, 7, 8]
