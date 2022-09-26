import math

#   INTEGRAIS
#           REGRA DOS TRAPEZIOS
# Entrada: funcao f, ponto a, ponto b,, ponto c, ponto d, numPontosParticao1, numPontosParticao2

def double_trapezio(f, a:float, b:float, c:float, d:float, n1:int, n2:int) -> float:
   if n1 <= 0 or n2 <= 0:
      raise ValueError("Não pode")
   h1 = (b - a) / n1
   h2 = (d - c) / n2

   soma_interior = 0
   for i in range(1, n1):# N1 é a qtde de subintervalos
      for j in range(1, n2):
         soma_interior += f(a + i * h1, c + j * h2)

   soma_aresta_horizontal = 0
   for i in range(1 ,n1): # ignora o ponto 0 e ponto n1
      for j in [0, n2]: # só considera os pontos 0 e n2
         soma_aresta_horizontal += f(a + i * h1, c + j * h2)

   soma_aresta_vertical = 0
   for j in range(1 ,n2):
      for i in [0, n1]:
         soma_aresta_vertical += f(a + i * h1, c + j * h2)

   soma_vertice = 0
   for i in [0 ,n1]:
      for j in [0, n2]:
         soma_vertice += f(a + i * h1, c + j * h2)

   return (h1 * h2 / 4) * (soma_vertice + 4 * soma_interior + 2 * (soma_aresta_horizontal + soma_aresta_vertical))

# def f(x,y):
#    return math.exp(-x**2 - y ** 2)

# a,b = [1, 2]
# c,d = [-1, 0]
# n1, n2 = 1000, 2000

#--------------------------------------------------------------------------
#EX 68
# def f(x,y):
#    return math.e**-(x**2+y**2) * math.cos(x) + 1

# intervalo1 = [-1.57, 1.003]
# intervalo2 = [-1.426, 1.322]
# n1 = 6
# n2 = 8
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 69
# def f(x,y):
#    return math.sqrt(math.e**-(x**2 * y**2) + 1)

# intervalo1 = [-1.723, 1.088]
# intervalo2 = [-1.18, 1.406]
# n1 = 10
# n2 = 21
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 69
# def f(x,y):
#    return math.cos(x**2)*math.sin(y**2*x)*math.e**-(y**2) + 1

# intervalo1 = [-1.05, 1.043]
# intervalo2 = [-1.438, 1.431]
# n1 = 37
# n2 = 16
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX 70
# def f(x,y):
#    return math.cos(x**2 + y) + 2

# intervalo1 = [-1.467, 1.863]
# intervalo2 = [-1.795, 1.539]
# n1 = 89
# n2 = 57
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX P2.9
def f(x,y):
   return math.cos(x**2)*math.sin(x*y**2)*math.e**-(y**2) + 1

intervalo1 = [-1.612, 1.942]
intervalo2 = [-1.7, 1.28]
n1 = 37
n2 = 16
#--------------------------------------------------------------------------

def f(x,y):
   return math.e ** (-(x+y)**2)

intervalo1 = [-1.15, 0.694]
intervalo2 = [-0.974, 0.95]
n1 = 8
n2 = 7

if __name__ == "__main__":
   res=double_trapezio(f, intervalo1[0], intervalo1[1],intervalo2[0], intervalo2[1], n1, n2)
   print(res)

