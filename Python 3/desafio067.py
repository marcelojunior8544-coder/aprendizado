# tabuada v3 / para ao digitar um número negativo
from time import sleep
while True:
    n = int(input('Digite um número positivo para ver sua tabuada: '))
    if n < 0:
        break
    print('-='*10)
    for c in range(1, 11):
        print(f'{n} x {c:^2} = {n * c}')
    print('-='*10)
print('Só um segundo, finalizando o programa.')
sleep(1)
print('Obrigado por usar o programa. Volte sempre')
