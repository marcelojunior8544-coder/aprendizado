# números aleatórios em um tupla
from random import randint
tupla = tuple(randint(0, 10) for c in range(5))
print(f'Os valores sorteados foram: ', end=' ')
for c in tupla:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
