import math

#   O método é utilizado para aproximar soluções de sistemas lineares
#   1 passo: isole uma variavel
#   SISTEMAS LINEARES
#           METODO DE JACOBI
# Entrada: matriz[lin][col], termosIndependentes[col], chute[col], numIteracao
# matriz é o sistema linear
# TI são as respostas em vetor do das equacoes do Sistema Linear
#chute são os pontos x,y,z iniciais

def metodoJacobi(matriz,ti,chute,numIteracao):
  linha=len(matriz)
  coluna=len(matriz[0])
  for it in range(numIteracao):
    tmp = []
    for i in range(linha):
      xi = float(ti[i])
      for j in range(coluna):
        if i != j:
          #xi -= matriz[j] * chute[j]  == x1 = x1 - ()
          xi = float (xi - (matriz[i][j] * chute[j]))
      #xi /= a[i] == x1 = x1/a[i]
      xi = float(xi / matriz[i][i])
      tmp.insert(i, xi)
    print("X^{} -> ".format(it+1))
    for k in range(coluna):
      print("{}".format(tmp[k]))
      chute.insert(k,tmp[k])
    print("")

if __name__ == "__main__":

###############################################

# QUESTÃO 25
  # A = [[-5.14, -0.61, -2.64], [4.93, -9.04, -2.22], [1.8, -0.72, 4.4]]
  # B = [-3.81, 3.51, 3.14]
  # chute = [-1.65, -0.75, 1.48]
  # n = 18

###############################################

# QUESTÃO 26

  A = [
    [-7.31, 0.47, 3.61, -1.23],
    [0.59,9.33,2.35,4.39],
    [0.17,1.37,-6.63,3.09,],
    [-3.5,4.54,4.71,14.74]]
  B = [-4.01, -1.14, 4.56, 2.1]
  chute = [0.42,4.28,-4.47,-3.41]
  n = 16

###############################################

  # A = [[-10.9764, -4.1375, -4.84267], [2.26031, 7.17403, -2.9175], [3.11381, -3.38176, -8.4918]]
  # B = [1.47595, 0.40306, 2.30515]
  # chute = [1.37329, -4.93343, 1.64169]
  # n=18

  # a     = [[6,1,-1,1],[1,-7,1,2],[2,1,9,-2],[1,2,1,-10]]
  # b     = [7,-10,-3,2]
  # chute = [0,0,0,0]
  # n     = 20

  metodoJacobi(A,B,chute,n)
