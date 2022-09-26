import math

#######################
# ARQUIMEDES!
# esse arquivo cospe a função a ser utilizada nos outros algoritmos


r1 = 2.68
r2 = 7.35
H = 3.86
Pw = 1000
Pt = 423.72
pi = math.pi
r3 = f'({r1}+x*({r2}-{r1})/{H})'
Hdiff = f'({H}-x)'
V = f'(({pi}*{H})/3.0)*(({r1}**2)+({r2}**2) + {r1}*{r2})'
Vw = f'(({pi}*{Hdiff})/3.0)*({r3}**2)+({r2}**2) + {r3}*{r2})'

F = f'{Pw}*{Vw} - {Pt}*{V}'

print(F)


##########################
