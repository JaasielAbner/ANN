import math

i = 3
x = 7.7871
n = 0

for n in range(0,i+1):
    sum = sum + 3 * math.cos((x**2-1)**(1/3))

print("{:.20f}".format(sum))