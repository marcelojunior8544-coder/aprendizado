# Criar uma lista e separar os pares dos ímpares
lista = []
pares = []
impares = []

#Preenchendo a lista principal
while True:
    numero = int(input('Digite um número; '))
    lista.append(numero)
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    # Verificar resposta do usuário
    while continuar not in 'SN':
        print('Resposta inválida.', end = ' ')
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

# Separando pares de ímpares
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
