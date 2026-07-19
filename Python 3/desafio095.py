# jogador v2
jogadores = []
dados = {}
while True:
    dados['nome'] = str(input('Nome do jogador: ')).strip().title()
    dados['gols'] = []
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(1, partidas + 1):
        gols = int(input(f'Quantos gols na partida {c}? '))
        dados['gols'].append(gols)
    dados['total'] = sum(dados['gols'])
    jogadores.append(dados.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break

print('-='*30)
print(f'{"cod":4} {"nome":<15} {"gols":<15} {"total":<15}')
print('-'*40)
for i, v in enumerate(jogadores):
    print(f'{i:4}', end = ' ')
    print(f'{v["nome"]:<15}', end = ' ')
    print(f'{str(v["gols"]):<15}', end = ' ')
    print(f'{v["total"]:<15}', end = ' ')
    print()

print('-'*40)
resp = int(input('Quer mostrar os dados de qual jogador? '))
while resp != 999:
    print(f' --Levantamento do jogador {jogadores[resp]["nome"]}')
    for i, g in enumerate(jogadores[resp]["gols"]):
        print(f'    No jogo {i+1} fez {g} gol(s)')
    resp = int(input('Quer mostrar os dados de qual jogador? '))
    