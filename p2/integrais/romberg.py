
import math

#   INTEGRAIS
#           REGRA DE ROMBERG
# O método de Integração é o método de extrapolação de
# Richardson aplicado sobre a Regra dos Trapézios

def trapezio(f, a, b, h): #F1 e recebe
   n = int ((b - a) / h) #Calcula o numero de subintervalos
   soma = 0
   for k in range(1,n):#comecar em 1 evitando que o primeiro ponto seja calculado 2 vezes
      soma += f(a + k * h)
   return (h / 2) * (f(a) + 2 * soma + f(b))

def romberg(col1):
   col1 = [item for item in col1]
   n = len(col1)
   for j in range(n - 1):
      tmp_coluna = [0] * (n - 1 - j)
      for i in range(n - 1 - j):
         power = j + 1 # é igual ao num da coluna anterior
         tmp_coluna[i] = (4 ** power * col1[i + 1] - col1[i]) / (4 ** power - 1)
      col1[:n - 1 - j] = tmp_coluna
      print(f'F_{j+2}', tmp_coluna)
   return col1[0] #a aprox. procurada

# def f(x):
#    return math.exp(-x ** 2)

# a,b   = [0, 1]
# h     = 0.5
# k     = 5
# hs    = [h / 2 ** i for i in range(k)]
# col1  = [trapezio(f, a, b, hi) for hi in hs]

#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
# #EX 62
# def F(x):
#    return math.sqrt(1+math.cos(x)**2)
# a, b = [-1.792, -0.792]
# ##O(4) -> h = 2 | O(8) -> H = 4 | O(12) -> h = 6?
# h = 1
# k = 3
# hs    = [h / 2 ** i for i in range(k)]
# col1  = [trapezio(F, a, b, hi) for hi in hs]
# #--------------------------------------------------------------------------
# #--------------------------------------------------------------------------
# #EX 65
# def F(x):
#    return math.sin(x/(math.sqrt(x**2+1))) + 1

# a, b = [-1.442, 1.662]
# ##O(4) -> h = 2 | O(8) -> H = 4 | O(12) -> h = 6?
# h = 1
# k = 3
# col1=[3.140402113058976, 3.291559552489043, 3.2670334619593633]
# #--------------------------------------------------------------------------
# #--------------------------------------------------------------------------
# #EX 66
# def F(x):
#    return math.sqrt(1+math.cos(x)**2)

# a, b = [-1.854, 1.302]
# ##O(4) -> h = 2 | O(8) -> H = 4 | O(12) -> h = 6?
# h = 1
# k = 5
# col1=[3.2711481634748645, 3.8253802783902255, 3.8358850964772127, 3.8352742133767794, 3.835166198665814]
# #--------------------------------------------------------------------------
# #--------------------------------------------------------------------------
# #EX 67
# def F(x):
#    return math.sqrt(math.sin(math.cos(math.log(x**2+1)+2)+3)+4)

# a, b = [-1.476, 1.555]
# ##O(4) -> h = 2 | O(8) -> H = 4 | O(12) -> h = 6?
# h = 1
# k = 6
# col1=[6.715204734024023, 6.583329589315438, 6.609051587156075, 6.609504221273691, 6.6095854474202005, 6.609605374955651]
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#EX P2.8
# def F(x):
#    return math.sqrt(1+math.cos(x)**2)

# a, b = [-1.678, 1.345]
# h = 1
# k = 5
# col1=[3.0690453207427417, 3.6573774502304492, 3.6944182338364344, 3.698630605113844, 3.699604634330561]
#--------------------------------------------------------------------------

#####################################

# def f(x):
#    a = 0.48
#    b = -0.55
#    c = 0.18
#    return (9 + 4 * (math.cos(a*x))**2) * (5 * (math.e)**(b*x) + 2 * math.e**(c*x))

def f(x):
    return -x*(x-21)*(x+1)

a,b = [0,12]
h = 12/10
k = 8

# #####################################

# def f(x):
#     return math.sqrt(1+x**2)

# a,b = [0.61,1.61]
# h = 0.5
# k = 8

# #####################################

# def f(x):
#     return math.cos(-x**2/3)

# a,b = [0.06,1.06]
# h = 0.5
# k = 6

# #####################################

# def f(x):
#     return math.exp(-x**2)

# a,b = [-1.28,-0.28]
# h = 0.125
# k = 10

#####################################

# def f(x):
#     return math.exp(x)*math.sin(x)/(1+x**2)

# a,b = [0.65,1.65]
# h = 0.25
# k = 8

#####################################

hs    = [h / 2 ** i for i in range(k)]
col1  = [trapezio(f, a, b, hi) for hi in hs]

if __name__ == "__main__":
   # print('F_1', col1)
   r=romberg(col1)
   #print(f'o numero {r} é aprox. para integral em [{a},{b}], com erro O(h^(2*{k})')
