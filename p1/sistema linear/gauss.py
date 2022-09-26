import math

#   O método da eliminação de Gauss para resolver sistemas lineares consiste em transformar a matriz dos coeficientes de um SL num matriz triangular superior
#   Para 'zerar' os elementos abaixo da diagonal de uma matriz, usamos o que chamamos de pivôs. Pivôs são elementos não nulos da diagonal de uma matriz.
#   Se um elemento a_ii for != 0, ele pode ser um pivô. Agora se a_ii == 0, precisamos encontrar o primeiro elemento abaixo de a_ii que seja não nulo e trocar a linha de a_ii pela linha deste elemento
#########################################################
#           METODO DA ELIMINACAO DE GAUSS
# Entrada: matriz[lin][col]

def printMatriz(matriz):
  linha=len(matriz)
  coluna=len(matriz[0])
  for i in range(linha):
    for j in range(coluna):
      print("{}\t".format(matriz[i][j]))
    print("\n")

def metodoGauss(matriz):
  linha=len(matriz)
  coluna=len(matriz[0])
  for j in range(linha-1):
    p = j
    for p in range(linha):
      if(matriz[p][j] != 0):
        if(p != j):
          #troca as linhas p e j
          tmp=0
          for k in range(coluna):
            tmp = matriz[j][k]
            matriz[j][k] = matriz[p][k]
            matriz[p][k] = tmp
            # matriz.insert(matriz[j][k],matriz[p][k])
            # matriz.insert(matriz[p][k],tmp)
        i = j+1
        for i in range(linha):
          print(matriz[j][j])
          a = -matriz[i][j] / matriz[j][j]
          for q in range(coluna):
            matriz[i][q] = ( a*matriz[j][q] ) + matriz[i][q]
            # tmp_2 = a * matriz[j][q] + matriz[i][q]
            # matriz.insert([i][q],tmp_2)
    print(matriz)
    print("\n\n")

if __name__ == "__main__":
  #matriz  = [[1,2,3,1],[1,5,3,1],[1,4,-1,1]]
  matriz = [[1, 1.037, 1.075369, 1.115157653, 1.156418486161], [1, 1.939, 3.759721, 7.290099019, 14.135501997841],
       [1, 3.019, 9.114361, 27.516255859, 83.071576438321], [1, 5.197, 27.008809, 140.364780373, 729.475763598481],
       [1, 6.612, 43.718544, 289.067012928, 1911.311089479936]]
  metodoGauss(matriz)
