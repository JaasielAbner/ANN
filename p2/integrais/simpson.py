
import math

#   INTEGRAIS
#           REGRA DE SIMPSON
# Entrada: funcao f, ponto a, ponto b, numSubIntervalosParticao

def simpson(f, a, b, n):
   if n % 2 != 0 or n < 1:
      raise ValueError("n deve ser par e maior que 1")
   h = (b - a) / n
   #  particao = [a + k * h for k in range(n + 1)]
   #  particao_impar = [a + k * h for k in range(1, n , 2)]
   #  particao_par = [a + k * h for k in range(1, n + 1, 2)]
   soma_impar, soma_par = 0, 0
   for k in range(1, n, 2): #Estamos considerando somente indice impar
      soma_impar += f(a + k * h)
   for k in range(2, n, 2): #Estamos considerando somente indice par
      soma_par += f(a + k * h)
   return (f(a) + 4 * soma_impar + 2 * soma_par + f(b)) * (h / 3)

# def f(x):
#    a = 0.48
#    b = -0.55
#    c = 0.18
#    return (9 + 4 * (math.cos(a*x))**2) * (5 * (math.e)**(b*x) + 2 * math.e**(c*x))

def f(x):
    return -x*(x-21)*(x+1)

# a,b = [0.544,3.973]
# n = 6 #numero de subintervalos
# #--------------------------------------------------------------------------
# #--------------------------------------------------------------------------
# #EX 56
# # def f(x):
# #    return math.e**(-x**2)
# # a,b = [-0.637, 0.662]
# #subintervalos = [4, 24, 40, 52, 76, 118, 212, 392, 610, 772, 1056]
# #--------------------------------------------------------------------------
# #--------------------------------------------------------------------------
# #EX 5-
# x = [0.004, 0.072, 0.14, 0.3425, 0.545, 0.5485, 0.552, 0.614, 0.676, 0.777, 0.878, 0.93, 0.982, 1.038, 1.094, 1.317, 1.54, 1.8765, 2.213, 2.234, 2.255, 2.7175, 3.18, 3.2265, 3.273, 3.2915, 3.31, 3.3535, 3.397, 3.4875, 3.578, 3.6295, 3.681, 3.796, 3.911, 4.0165, 4.122, 4.172, 4.222, 4.5665, 4.911]
# y = [1.254, 1.456, 1.687, 2.384, 2.854, 2.86, 2.865, 2.939, 2.983, 2.997, 2.952, 2.911, 2.861, 2.799, 2.732, 2.45, 2.21, 2.015, 2.045, 2.055, 2.065, 2.492, 2.984, 2.998, 2.999, 2.995, 2.989, 2.966, 2.928, 2.801, 2.606, 2.467, 2.311, 1.916, 1.512, 1.202, 1.022, 1.0, 1.025, 2.299, 2.814]

# #--------------------------------------------------------------------------
# #--------------------------------------------------------------------------
# #EX P2.7
# x = [0.888, 0.9055, 0.923, 1.2705, 1.618, 1.831, 2.044, 2.5905, 3.137]
# y = [2.945, 2.931, 2.917, 2.507, 2.145, 2.029, 2.002, 2.342, 2.962]
# #--------------------------------------------------------------------------

# x = [0.544, 1.812, 2.169, 3.188, 3.436, 3.631, 3.973]
# y = [2.853, 2.035, 2.029, 2.987, 2.882, 2.463, 1.318]

# #--------------------------------------------------------------------------
# #--------------------------------------------------------------------------

# x = [1.923, 2.495, 3.067, 3.118, 3.169]
# y = [2.006, 2.243, 2.908, 2.949, 2.979]

# #--------------------------------------------------------------------------
# #--------------------------------------------------------------------------

# x = [0.2, 0.31, 0.42, 0.483, 0.546, 0.5565, 0.567, 0.638, 0.709, 0.7795, 0.85, 0.883, 0.916, 0.9845, 1.053, 1.1925, 1.332, 1.468, 1.604, 1.844, 2.084, 2.134, 2.184, 2.3825, 2.581, 2.667, 2.753, 2.7895, 2.826, 2.9, 2.974, 3.1635, 3.353, 3.421, 3.489, 3.6245, 3.76, 4.1865, 4.613, 4.618, 4.623, 4.691, 4.759, 4.8665, 4.974]
# y = [1.902, 2.282, 2.601, 2.745, 2.856, 2.871, 2.886, 2.96, 2.995, 2.997, 2.969, 2.948, 2.923, 2.858, 2.781, 2.607, 2.432, 2.279, 2.156, 2.024, 2.007, 2.018, 2.034, 2.146, 2.331, 2.43, 2.537, 2.584, 2.631, 2.724, 2.813, 2.977, 2.966, 2.901, 2.798, 2.482, 2.044, 1.002, 2.518, 2.54, 2.562, 2.818, 2.971, 2.935, 2.548]

# x = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0]
# y = [0.0, 1.3,2.08,3.24,4.19,5.07,6.25,7.04,8.05,8.85,9.37,10.94,11.48]

# x = [0.0, 10.0/3600,20.0/3600,30.0/3600,40.0/3600,50.0/3600,60.0/3600]
# y = [121.73,248.79,179.88,154.28,235.3,288.4,209.66]

# x = [0.0, 0.75,1.5,2.25,3.0,3.75,4.5,5.25,6.0,6.75,7.5,8.25,9.0,9.75,10.5,11.25,12.0]
# y = [9.75,9.35,9.11,8.6,8.11,7.61,7.46,6.86,6.48,5.93,5.71,5.29,4.95,4.5,4.18,3.67,3.22]

# x = [0.0/3600, 5.0/3600,10.0/3600, 15.0/3600,20.0/3600,25.0/3600,30.0/3600,35.0/3600,40.0/3600,45.0/3600,50.0/3600,55.0/3600,60.0/3600,65.0/3600,70.0/3600,75.0/3600,80.0/3600,85.0/3600,90.0/3600]
# y = [0,108,228,358,515,668,818,970,1091,1211,1316,1465,1635,1821,2046,2314,2604,2896,3205]

a = 0
b = 12
n = 14

if __name__ == "__main__":
   print(simpson(f, a, b, n)) #simples
   #for i in range(len(subintervalos)):#57
      #print(subintervalos[i],simpson(f,intervalos[0],intervalos[1],subintervalos[i]))
   #   print(simpson(f,a,b,subintervalos[i]))#57
   # sum = 0.0
   # for n in range(2,len(x),2):
   #    sum += ((x[n-1] - x[n-2])/3) * (y[n-2] + 4*y[n-1] + y[n])
      #print('{} -- ({},{})'.format(i,x[i],y[i]))
   print(sum)

