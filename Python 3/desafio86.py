# criando um matriz
matriz = [[], [] , [], []]
from random import randint
sDP = 0
p2l = 1
# inserindo os valores na matriz
for i in range(0, 4):
    for c in range(0, 4):
     #matriz[i].append(int(input(f'Digite um valor para {i}, {c}: ')))
        matriz[i].insert(c, randint(2,10))
        if i == c:
            sDP += matriz[i][c]
        if i == 2:
            p2l *= matriz[i][c]
# mostrando a matriz
for i in range(0, 4):
    print(f'[{matriz[i][0]:^5}] [{matriz[i][1]:^5}] [{matriz[i][2]:^5}] [{matriz[i][3]:^6}]')
print(f'A soma da diagonal principal é {sDP}')
print(f'O produto da segunda linha é {p2l}')
