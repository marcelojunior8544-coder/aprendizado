# jogo de adivinhar v2
from random import randint
from time import sleep
num = randint(0,10)
print('*='*25)
print('{:^60}'.format('Vou pensar em um numero entre 0 e 10.'))
print('{:^60}'.format('E você vai tentar adivinhar'))
print('*='*25)
print('Pensando...')
sleep(1)
tent = 0
acertou = False
while not acertou:
    jog = int(input('Em que número eu pensei? '))
    tent += 1
    if jog != num:
        if jog < num:
            print('É maior, ', end=' ')
        else:
            print('É menor. ', end=' ')
        print('tente novamente.')
    else:
        acertou = True

if tent > 1:
    print("Você acertou em {} tentativas".format(tent))
else:
    print('Você acertou de primeira!!')
