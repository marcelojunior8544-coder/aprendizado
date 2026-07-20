#
numeros = []
from random import randint
from time import sleep

def sorteia(n):
    print(f'Sorteando {n} valores.')
    for c in range(0, n):
        num = randint(1, 10)
        numeros.append(num)
        print(num, end = ' ', flush=True)
        sleep(0.5)
    print('FIM')


def somaPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    return soma


sorteia(5)
print(f'Somando os valores pares de {numeros}, temos {somaPar(numeros)}')
