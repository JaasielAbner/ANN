import math

####--####--####--####--####--##
#Exercise 1
# def f(x):
#   return x**2 - 3

# a = -2.48453
# b = -0.74369

####--####--####--####--####--##
#Exercise 2
#def f(x):
#   return x**2 - 4*x +2 - math.log(x)
# a = 0.26115
# b = 1.83549

####--####--####--####--####--##
#Exercise 3
# def f(x):
#   return math.exp(x) - 2*x**2 +x -1.5
# a = 1.64464
# b = 2.60854

####--####--####--####--####--##
#Exercise 4
#def f(x):
#   return x**2 - 7
# a = -3.2867
# b = -2.02933

####--####--####--####--####--##
#Exercise 5
#def f(x):
#   return x**2 - 5
# a = -2.78116
# b = -1.63452

####--####--####--####--####--##
#Exercise 6
#def f(x):
#   return x**4 -2*x**3 -3*x**2 +3*x + 2
# a = -0.96755
# b = 0.27804

####--####--####--####--####--##
#Exercise 7
# def f(x):
#   return x**3 - 7*x**2 + 14*x - 7
# a = 0.32818
# b = 4.29568
####--####--####--####--####--##

###--####--####--####--####--##
# Exercise 29

# def f(x):
   # v=32.3
   # g=9.81
   # c=24.08
   # t=7.63
   # return math.log(g)-math.log(c)-math.log(v) + math.log(x) + math.log(1-math.e**(-(c/x)*t))

# a=39.09
# b=205.18
# numIteracao = 20
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# Exercise 30

# def f(x):
   # g=9.81
   # m=70.73
   # v=26.44
   # t=7.18
   # return math.log(g)-math.log(x)-math.log(v) + math.log(m) + math.log(1-math.e**(-(x/m)*t))

# a=1
# b=100
# numIteracao = 14
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# Exercise 31

# def f(x):
   # g=9.81
   # v=9.35
   # t=4.71
   # l=3.37
   # return (math.sqrt(2*g*x)*math.tanh((math.sqrt(2*g*x)/2*l)*t)/v)-1

# a=0
# b=6
# numIteracao = 15
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# Exercise 32

# def f(x):
   # q=158.06
   # g=9.81
   # b=1.56+x
   # ac=1.56*x+x**2/2
   # return 1 - ((q**2/g*ac**3)*b)
   # return -(q**2/(g*ac**3)*b) + 1
# a=0.1
# b=8
# numIteracao = 13
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# Exercise 33

# def f(x):
   # r=7.74
   # v=480.18
   # p1=math.pi*x**2
   # p2=(3*r-x)/3
   # return ((math.pi*x**2*((3*r-x)/3))/v) - 1
# a=0
# b=15.48
# numIteracao = 11
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# Exercise 34

# def f(x):
   # r=3.5
   # ps=464.59
   # pw=1000
   # vs=(4*math.pi*r**3)/3
   # v=(math.pi*x**2/3)*(3*r-x)
   # # print("vs=={}||=={}\n".format(vs,v))
   # return ((pw*(vs-v))/(ps*vs)) - 1

# r=3.5
# a=0
# b=2*r
# numIteracao = 15
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# Exercise 35

# def f(x):
#    p0=1346395
#    v=389644
#    p=3419631
#    t=1
#    return (p0*(math.e**(x))) -p + ((v/x)*((math.e**x) -1))

# a=0.1
# b=1
# numIteracao = 13
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# Exercise 36

# def f(x):
#    l=4.56
#    r=4.77
#    v=76.54
#    r2=r**2
#    tmp=r-x
#    tmp2=(r**2)-(2*r*x)+(x**2)
#    return -v+(l*( (0.5*math.pi*r2) -
#           (r2*math.asin(tmp/r)) - (tmp*math.sqrt(r2-tmp2))))

# r=4.77
# a=0
# b=r
# numIteracao = 15
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# Exercise 37

# def f(x):

#   g=9.81
#   return -(9.81 / (2*(x**2))) * (math.sinh(x) - math.sin(x)) -1.81
# a=-4.87
# b=-0.25
# numIteracao = 11
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# Exercise 38

# def f(x):
#    aa=12
#    bb=-111.8
#    cc=171.8266
#    return aa*x**2 + bb*x + cc
# a=0
# b=4.57
# numIteracao = 12
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# PROVA - 1

# def f(x):
#   return x**3 - 7*x**2 + 14*x - 7
# a=0.21106
# b=4.39613
# numIteracao = 5
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# PROVA - 6

# def f(x):
#    r=3.66
#    ps=88.63
#    pw=1000
#    vs=(4*math.pi*r**3)/3
#    v=(math.pi*x**2/3)*(3*r-x)
#    return ((pw*(vs-v))/(ps*vs)) - 1

# r=3.66
# a=0
# b=2*r
# numIteracao = 15
# err=0
###--####--####--####--####--##
###--####--####--####--####--##
# PROVA - 7

# def f(x):
#    l=1.81
#    r=1.42
#    v=3.65
#    r2=r**2
#    tmp=r-x
#    tmp2=(r**2)-(2*r*x)+(x**2)
#    return -v+(l*( (0.5*math.pi*r2) -
#           (r2*math.asin(tmp/r)) - (tmp*math.sqrt(r2-tmp2))))

# r=1.42
# a=0
# b=r
# numIteracao = 15
# err=0

###--####--####--####--####--##
###--####--####--####--####--##
# PROVA - 5

# def f(x):
#   lbnd=1.41*(10**-10)
#   n=146775524
#   xt=n*0.25
#   p1=n+1
#   p2=1 + n*math.e**((-lbnd*n -lbnd)*x)
#   #return (n+1/(1+n*math.e**(-lbnd*(n+1)*x))) - xt
#   return (p1/p2) - xt
# a=0
# b=1818
# numIteracao = 15
# err=0

###--####--####--####--####--##
###--####--####--####--####--##
# PROVA - 8

# def f(x):
#   return 1000*((math.pi*(9.8-x))/3.0)*(pow((1.21+x*(7.07-1.21)/9.8),2)+pow(7.07,2) + (1.21+x*(7.07-1.21)/9.8)*7.07) - 343.94*((math.pi*9.8)/3.0)*(pow(1.21,2)+pow(7.07,2) + 1.21*7.07)
# a=0
# b=9.8
# numIteracao = 12
# err=0

###--####--####--####--####--##

# def f(x):
#   return 1586191*(math.e)**x + (219635/x)*(math.e**(x)-1) - 3406533

# a = 0.1
# b = 1.07
# numIteracao = 12
# err = 0

###--####--####--####--####--##

# def f(x):
#   a = 7.53 * x + (x**2)/2
#   b = 7.53 + x
#   return 1 - (((145.29)**2)/9.81*(a)**3) * b

# a = 0.49
# b = 8.21
# numIteracao = 12
# err = 0

###--####--####--####--####--##

# def f(x):
#   g = 9.81
#   q = 145.29
#   A = 7.53*x + ((x*x)/2)
#   B = 7.53 + x
#   return 1 - (((q*q)/(g*(A*A*A))))*B

# a = 0.49
# b = 8.21
# numIteracao = 12
# err = 0

###--####--####--####--####--##

def f(x):
  v = 57.55
  r = 3.17
  return math.pi*(x**2)*((3*r - x)/3) - v

a = 0
b = 6.34
numIteracao = 12
err = 0

###--####--####--####--####--##

#   ZERO DE FUNCAO
#           METODO DA BISSECAO
# Entrada: estimativa inicial (a), estimativa inicial 2 (b) funcao (f), precisão (err) e numero de iteracoes (numIteracao)

def bissecao(a,b,f,err,numIteracao):
  print("f(a) * f(b) = {0}\n" .format(f(a)*f(b)) )
  if f(a) * f(b) < 0:
    midPoint = (a+b)/2
    for x in range(numIteracao):
      if (math.fabs(f(midPoint)) > err):
        midPoint = (a+b)/2
        if f(midPoint) == 0 or (math.fabs(f(midPoint)) < err):
          print("A raiz e: {0}\n\n".format(midPoint))
        else:
          if f(a) * f(midPoint) < 0:
            b = midPoint
          else:
            a = midPoint
      else:
        print("A raiz e: {0}\n\n".format(midPoint))
        break
      print("x_{0} = {1} \t f->{2}".format(x+1, midPoint, (math.fabs(f(midPoint))) ))
  else:
    print("Nao ha raiz neste intervalo!")

if __name__ == "__main__":
  #bissecao(a,b,f,err,numIteracao)
  bissecao(inferior1, superior1, f, err, numIteracao)
