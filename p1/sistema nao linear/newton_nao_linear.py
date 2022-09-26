import math

# #Pegar as funcoes e deixar como equacao=0
# #e1 = x**2 + 2*y**2 = 3
# #e2 = 4*x**2 + y**2 = 6
# f  = x**2+2*y**2-3,,,,4*x**2+y**2-6
# #calcular a derivada de f(x,y) -->[ [derivada de f1 em relacao a x] [derivada de f1 em relacao a y]
# #                                   [derivada de f2 em relacao a y] [derivada de f2 em relacao a y] ]
# m = [2*x, 4*y, 8*x, 2*y]
# #calcular a matriz invertida de df_x --> [a] [b]
# #                                        [c] [d]

# # matrizInvertida = (1/detA) *     [+d] [-b]
# # detA=a*d-(b*c)                   [-c] [+a]
# #detA = m[0]*m[3] - (m[1]*m[2])
# detA = (4*x*y) - (32*x*y)
# matInv = (-1/(detA) * [2*y,-4*y,-8*x,2*x]
# Agora escolher um chute inicial

###########################
# Exercício 47
# def f1(x,y):
#   return x**2 + (2*y**2) - 3

# def f2(x,y):
#   return (4*x**2) + y**2 - 6

# def f1x(x,y):
#   return 2*x

# def f2x(x,y):
#   return 8*x

# def f1y(x,y):
#   return 4*y

# def f2y(x,y):
#   return 2*y
###########################
###########################
# Exercício 48
# def f1(x,y):
#   return (4*x**2) + y**2 - 5

# def f2(x,y):
#   return x**2 + y**3 - 4

# def f1x(x,y):
#   return 8*x

# def f2x(x,y):
#   return 2*x

# def f1y(x,y):
#   return 2*y

# def f2y(x,y):
#   return 3*y**2
###########################
###########################
# Exercício 49
# def f1(x,y):
#   return x**2 + y**2 - 5

# def f2(x,y):
#   return x**2 + x*y**3 - 3

# def f1x(x,y):
#   return 2*x

# def f2x(x,y):
#   return 2*x + y**3

# def f1y(x,y):
#   return 2*y

# def f2y(x,y):
#   return 3*x*y**2
###########################
###########################
# Exercício 50
# def f1(x,y):
#   return x**2 + y**2 - 1

# def f2(x,y):
#   return x - y

# def f1x(x,y):
#   return 2*x

# def f2x(x,y):
#   return 1

# def f1y(x,y):
#   return 2*y

# def f2y(x,y):
#   return -1
###########################
###########################
# PROVA - 11

def f1(x,y):
  return (4*x**2) + y**2 - 5

def f2(x,y):
  return x**2 + y**3 - 4

def f1x(x,y):
  return 8*x

def f2x(x,y):
  return 2*x

def f1y(x,y):
  return 2*y

def f2y(x,y):
  return 3*y**2
################################
################################
################################
def det(x,y):
  return f1x(x,y) * f2y(x,y) - f1y(x,y) * f2x(x,y)

def eq1(x,y):
  return x - (1 / det(x,y)) * (f2y(x,y) * f1(x,y) - f1y(x,y) * f2(x,y) )

def eq2(x,y):
  return y - (1 / det(x,y)) * (-f2x(x,y) * f1(x,y) + f1x(x,y) * f2(x,y))

x0 = 0.7324
y0 = 1.3758
n  = 4

if __name__ == "__main__":
  for i in range(n):
    x1 = eq1(x0,y0)
    y1 = eq2(x0,y0)
    print("x_{} = {} \t y_{} = {}".format(i+1,x1,i+1,y1))
    x0 = x1
    y0 = y1
