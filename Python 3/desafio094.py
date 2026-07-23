# dicionário com dado de pessoas
dados = dict()
pessoa = list()
soma = 0
while True:
    dados['Nome'] = str(input('Nome: ')).strip().title()
    dados['Idade'] = int(input('Idade: '))
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    pessoa.append(dados.copy())
    soma += dados['Idade']
    dados.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in 'NS':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

if len(pessoa) > 0:
    print('-='*30)
    print(f' - O grupo tem {len(pessoa)} pessoas.')
    media = soma / len(pessoa)
    print(f' - A média de idade é de {media:5.2f} anos.')
    print(' - As mulheres cadastradas foram:', end = ' ')
    for p in pessoa:
        if p['Sexo'] == 'F':
            print(f'{p["Nome"]}', end = ' ')
    print()
    print('-='*30)
    print('A lista de pessoas com idade acima da média foram:')
    for c in pessoa:
        if c['Idade'] > media:
            for k, v in c.items():
                print(f'{k} = {v}; ', end = ' ')
            print()
else:
    print('Não há pessoas cadastradas.')
print('<<< VOLTE SEMPRE! >>>')
