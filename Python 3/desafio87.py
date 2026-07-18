# trabalhando matrizes em Python
matriz = [[], [], []]
spar = 0
s3c = 0
m2l = 0
from random import randint

# entrada de valores
for l in range(0, 3):
    for c in range(0, 3):
        #matriz[l].append(int(input(f'Digite um valor para [{l}, {c}] ')))
        matriz[l].append(randint(1,20))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        if c == 2:
            s3c += matriz[l][c]
        if l == 1:
            if c == 0:
                m2l = matriz[l][c]
            elif matriz[l][c] > m2l:
                m2l = matriz[l][c]

# mostrando os resultados
print('-=' * 20)
for l in range(0, 3):
    print(f'[{matriz[l][0]:^5}] [{matriz[l][1]:^5}] [{matriz[l][2]:^5}]')
print('-=' * 20)
print(f'A soma dos valores pares é {spar}.')
print(f'A soma dos valores da terceira coluna é {s3c}.')
print(f'O maior número da segunda linha é {m2l}.')
print('-=' * 20)
