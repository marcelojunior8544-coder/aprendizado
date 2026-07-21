# sortear números e somar os pares

from random import randint
from time import sleep

def sorteia(lst):
    print(f'Sorteando 5 valores.')
    for c in range(0, 5):
        num = randint(1, 10)
        lst.append(num)
        print(num, end = ' ', flush=True)
        sleep(0.5)
    print('FIM')


def somaPar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {numeros}, temos {soma}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)
