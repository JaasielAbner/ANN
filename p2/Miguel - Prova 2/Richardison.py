import math

def richardison(col1):
    n = len(col1)
    col1 = [item for item in col1]

    for j in range(n - 1):     # percorrer as colunas
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j): # percorrer as linhas
            power = j + 1
            temp_col[i] = ((2 ** power) * col1[i + 1] - col1[i]) / (2 ** power - 1)
        col1[:n - 1 - j] = temp_col
        print(temp_col)
    return col1[0]

h = 0.5
x0 = 3.47878
aproximações = [-0.3246958824512376, -0.3304021990345234, -0.3319466193208882, -0.33233971461231704]
# lista de aproximações i.e. primeira coluna da tabela
print(richardison(aproximações))