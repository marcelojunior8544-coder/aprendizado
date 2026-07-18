# inserir e organizar quantidade indeterminada de valores
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))

    # verificando resposta válida
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        print('Resposta inválida!', end = ' ')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if continuar == 'N':
        break

print('-' * 30)

# quantos valores foram digitados
if len(lista) > 1:
    print(f'Foram adicionados {len(lista)} valores à lista.')
else:
    print(f'Foi adicionado {len(lista)} valor à lista.')

print('-=' * 30)

# verificando se o valor 5 está na lista
if 5 in lista:
    print('O valor 5 foi encontrado na lista nas posições:', end = ' ')
    for p, v in enumerate(lista):
        if v == 5:
            print(f'{p}', end = ' ')
    print()
else:
    print('O valor 5 não foi encontrado na lista.', end = ' ')
    print()

print('-=' * 30)

# organizando em ordem decrescente
lista.sort(reverse=True)
print('O valores em ordem decrescente são:', end=' ')
for c in lista:
    print(f'{c} ', end=' ')
print('\n','-' * 30)
