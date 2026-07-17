# par ou impar até o jogador perder e contar quantas vitórias
from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    jogador = int(input('Diga um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    resp= ' '
    v = 0
    pi = ' '
    if total % 2 == 0:
        result = 'P'
        pi = 'Par'
    else:
        result = 'I'
        pi = 'Impar'
    while resp not in 'PI':
        resp = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    if resp != result:
        print('Você perdeu!')
        print(f'Eu escolhi {computador} e {jogador} + {computador} = {total} que é {pi}')
        break
    else:
        print('Você Venceu!!')
        print(f'Eu escolhi {computador} e {jogador} + {computador} = {total} que é {pi}')
        print('Vamos jogar novamente')
        v += 1
print(f'GAME OVER! Você venceu {v} vezes.')
