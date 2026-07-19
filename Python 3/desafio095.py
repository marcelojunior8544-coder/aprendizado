# jogador v2
jogadores = []
dados = {}

# alimentando o programa
while True:
    jogadores.clear()
    dados['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    dados['gols'] = []
    for c in range(1, partidas + 1):
        gols = int(input(f'Quantos gols na partida {c}? '))
        dados['gols'].append(gols)
    dados['total'] = sum(dados['gols'])
    jogadores.append(dados.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break

# exibindo tabela de jogadores
print('-='*30)
print(f'{"cod":4} {"nome":<15} {"gols":<15} {"total":<15}')
print('-'*40)
for i, v in enumerate(jogadores):
    print(f'{i:4}', end = ' ')
    print(f'{v["nome"]:<15}', end = ' ')
    print(f'{str(v["gols"]):<15}', end = ' ')
    print(f'{v["total"]:<15}', end = ' ')
    print()

# verificar informação de um jogador específico
print('-'*40)
while True:
    resp = int(input('Quer mostrar os dados de qual jogador?(999 para parar) '))
    if resp == 999:
        break
    if resp >= len(jogadores) or resp < 0:
        print(f'Não existe jogador código {resp}. Tente novamente.')
    else:
        print(f' --Levantamento do jogador {jogadores[resp]["nome"]}')
        for i, g in enumerate(jogadores[resp]["gols"]):
            print(f'    No jogo {i + 1} fez {g} gol(s)')
    print('-'*30)
print('<< VOLTE SEMPRE! >>')
