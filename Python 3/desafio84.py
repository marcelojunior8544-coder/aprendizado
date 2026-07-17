# Tratando de listas para gerenciar dados de pessoas
pessoas = list()
dados = []
pesados = []
leves = []

#Adicionando pessoas à lista
while True:
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

# Verificando maior e menor peso na lista
for c in pessoas:
    if c[1] <= 70:
        leves.append(c[:])
    elif c[1] >=100:
        pesados.append(c[:])

print(f'Foi adicionados {len(pessoas)} pessoas a lista')
print(f'Tem {len(leves)} pessoas com até 70KG sendo elas: ', end = ' ')
for c in leves:
    print(f'{c[0]} ', end=' ')
print()
print(f'Tem {len(pesados)} pessoas com 100KG ou mais, sendo elas: ', end = ' ')
for c in pesados:
    print(f'{c[0]}', end = ' ')
