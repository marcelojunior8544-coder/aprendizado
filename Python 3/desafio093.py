# Aproveitamento de jogador
jogador = dict()
jogador['Nome'] = str(input('Nome: ')).strip().title()
partida = int(input('Partidas: '))
jogador['Gols'] = list()
for c in range(1, partida+1):
    gols = int(input(f'Quantos gols na partida {c}: '))
    jogador['Gols'].append(gols)
jogador['Total'] = sum(jogador['Gols'])

print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partida} partidas.')
for p, g in enumerate(jogador['Gols']):
    print(f'    => Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')
print('-='*30)
