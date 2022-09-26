g = 9.81
v = 8.41

m1 = 72.72
c1 = 8.34

m2 = 54.33
c2 = 15.87

m3 = 42.93
c3 = 19.78

R = 0
T = 0

x = m1*g - c1*v
y = m2*g - c2*v
z = m3*g - c3*v

print()

print('R' + ' - ' + str(m3) + '*a' + ' + 0T' + ' = ' + ' - ' + str(m3*g - c3*v))
print('-' + 'R' + ' - ' + str(m2) + '*a' + ' + ' +
      'T' + ' = ' + ' - ' + str(m2*g - c2*v))
print('0R' + ' - ' + str(m1) + '*a' + ' - ' +
      'T' + ' = ' + ' - ' + str(m1*g - c1*v))