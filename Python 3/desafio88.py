# palpites da Mega Sena
from random import randint
from time import sleep
num = []
palpites = int(input('Quer fazer quantos palpites? '))
sorteio = []

#sorteando os números
while palpites > 0:
    while True:
        n = randint(1, 60)
        if n not in num:
            num.append(n)
        if len(num) == 6:
            break
    sorteio.append(num[:])
    num.clear()
    palpites -= 1

# exibindo os palpites
print('=-'*30)
for c in range(0, len(sorteio)):
    print(f'O {c+1}º palpite foi {sorted(sorteio[c])}')
    sleep(0.5)
print('=-'*30)
