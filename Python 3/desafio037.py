# Conversor de base numerica
num = int(input('Digite um número: '))
base = str(input('Diga para qual a base (1 para binário, 2 para octal, 3 para hexadecimal: )')).strip()
if base == '1':
    print('{} em binário fica {}'.format(num, bin(num)[2:]))
elif base == '2':
    print('{} em octal fica {}'.format(num, oct(num)[2:]))
elif base == '3':
    print('{} em hexadecimal fica {}'.format(num, hex(num)[2:]))
else:
    print('Não foi informado para qual base converter.')
