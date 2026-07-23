# jogar dado para 4 jogadores e organizar do maior para o menor
from random import randint
from operator import itemgetter
from time import sleep
jogadores ={}

for c in range(1, 5):
    jogadores[f'Jogador {c}'] = randint(1, 6)

print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'    O {k} tirou {v} o dado.')
    sleep(1)

jogadores = dict(sorted(jogadores.items(), key = itemgetter(1), reverse = True))
print('Ranking dos jogadores:')
cont = 1
for k, v in jogadores.items():
    print(f'    {cont}º lugar: {k} com {v}.')
    cont += 1
    sleep(1)
