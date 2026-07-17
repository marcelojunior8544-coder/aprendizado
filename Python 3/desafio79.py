# Adicionar quantidade indeterminada de valores únicos a uma lista e ordenar-los
lista = []
while True:
    num = int(input('Digite um valor: '))
    # Verificando se já está na lista
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor Duplicado. Não será adicionado')
    continuar = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    # Verificando resposta
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
lista.sort()
print('-='*20)
print(f'Você digitou os valores: {lista}')
print('-='*20)
