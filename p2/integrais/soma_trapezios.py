x = [0.0/3600, 5.0/3600,10.0/3600, 15.0/3600,20.0/3600,25.0/3600,30.0/3600,35.0/3600,40.0/3600,45.0/3600,50.0/3600,55.0/3600,60.0/3600,65.0/3600,70.0/3600,75.0/3600,80.0/3600,85.0/3600,90.0/3600]
y = [0,108,228,358,515,668,818,970,1091,1211,1316,1465,1635,1821,2046,2314,2604,2896,3205]
soma = 0
xy = zip(x,y)

for a2,b2 in zip(x[1:],y[1:]): # lista de x e y removidos os primeiros elementos
    for a1, b1 in zip(x,y):
        soma += ((a2-a1) * (b2 + b1))/2
        x.pop(0) # removendo os primeiros elementos das listas de x e y
        y.pop(0)
        break

print('soma de verdade?', soma)