lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        print('Resposta inválida!', end = ' ')
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-='*30)
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica {lista}')
if 5 in lista:
    print('O valor 5 apareceu na lista.')
else:
    print('O valor 5 não apareceu na lista;')
print('-='*30)
