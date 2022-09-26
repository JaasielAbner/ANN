import math

# rad
def para_radianos(x):
    return x/180*math.pi

# taylor
def taylor(x, i):
    return math.pow(x, i)/math.factorial(i)

# sen
def calcula_seno(x, termos):
    y = 3
    z = 0
    while True:
        z = z - taylor(x, y)
        y = y + 2
        z = z + taylor(x, y)
        y = y + 2
        if y >= termos:
            break
    return x+z

# cos
def calcula_cosseno(x, termos):
    y = 2
    z = 0
    while True:
        z = z - taylor(x, y)
        y = y + 2
        z = z + taylor(x, y)
        y = y + 2
        if y >= termos:
            break
    return 1+z

# testa seno
print('testa seno:')
seno_math = math.sin(para_radianos(32))
seno_taylor = calcula_seno(para_radianos(32), 5)
print('math.sin: ' + str(seno_math))
print('taylor:   ' + str(seno_taylor))
print('')
# testa cosseno
print('testa cosseno:')
cosseno_math = math.cos(para_radianos(45))
cosseno_taylor = calcula_cosseno(para_radianos(45), 5)
print('math.sin: ' + str(cosseno_math))
print('taylor:   ' + str(cosseno_taylor))