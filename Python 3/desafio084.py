# Tratando de listas para gerenciar dado de pessoas
pessoas = list()
dados = []
mai = men = 0

#Adicionando pessoas à lista
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

# mostrando a lista
print(f'Foi adicionados {len(pessoas)} pessoas a lista')
print(f'O menor peso foi de {men}. Peso de: ', end = ' ')
for c in pessoas:
    if c[1] == men:
        print(f'{c[0]} ', end=' ')
print()
print(f'O maior peso registrado foi de {mai}. Peso de:', end = ' ')
for c in pessoas:
    if c[1] == mai:
        print(f'{c[0]}', end = ' ')
