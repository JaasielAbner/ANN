from jacobi import metodoJacobi
import math

#   SISTEMAS LINEARES
#           METODO DA ELIMINACAO DE GAUSS SEIDEL
# Entrada: matriz[lin][col], termosIndependentes[col], chute[col], numIteracao
# matriz é o sistema linear
# TI são as respostas em vetor do das equacoes do SL

def metodoGaussSeidel(matriz,ti,chute,numIteracao):
  linha=len(matriz)
  coluna=len(matriz[0])
  for it in range(numIteracao):
    for i in range(linha):
      xi = ti[i]
      for j in range(coluna):
        if i != j:
          xi -= matriz[i][j] * chute[j]
      xi /= matriz[i][i]
      chute[i] = xi
    #if it == 2 or it == 8 or it == 16:
    print("X^{} -> ".format(it+1))
    for k in range(coluna):
      print("{}".format(chute[k]))
    print("")

if __name__ == "__main__":
  A = [[1, -1,0], [-45.82,-62.28,-75.75], [0,1,-1]]
  B = [- 318.2694, - 510.42960000000005, - 683.2089000000001]
  chute = [0,0,0]
  n=1

  metodoGaussSeidel(A,B,chute,n)
