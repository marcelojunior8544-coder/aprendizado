nome = str(input('Digite o nome de uma pessoa: ')).strip()
if 'silva' in nome.lower().split():
    print('Esse nome possui Silva')
else:
    print('Esse nome não possui Silva.')
