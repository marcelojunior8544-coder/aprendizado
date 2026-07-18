# separar pares e ímpares v2
lista =[[], []]

# entrada de valores
for c in  range(0,7):
    num = (int(input(f'Diga o {c+1}º número: ')))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)

print('-~'*20)
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista[1])}')
