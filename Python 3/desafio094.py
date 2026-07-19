# dicionário com dados de pessoas
dados = dict()
pessoa = list()
soma = 0
while True:
    dados['Nome'] = str(input('Nome: ')).strip().title()
    dados['Idade'] = int(input('Idade: '))
    dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    while dados['Sexo'] not in 'MF':
        print('Sexo invalido. Tente novamente.')
        dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    pessoa.append(dados.copy())
    soma += dados['Idade']
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp not in 'SN':
        print('Resposta invalida.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break

if len(pessoa) > 0:
    media = soma / len(pessoa)
    print('-='*30)
    print(f' - O grupo tem {len(pessoa)} pessoas.')
    print(f' - A média de idade é de {media:.1f} anos.')
    print(' - As mulheres cadastradas foram:', end = ' ')
    for c in pessoa:
        if c['Sexo'] == 'F':
            print(f'{c["Nome"]}', end = ' ')
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