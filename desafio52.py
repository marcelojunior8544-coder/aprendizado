# verificar se um numero é primo
num = int(input('Digite um número: '))
d = 0
print('Esse número é divisível por:')
for c in range(1, num + 1):
    if num % c == 0:
        d += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c),end=' ')
if d > 2:
    print('\n\033[mEsse número foi divisível {} vezes, ele não é primo'.format(d))
else:
    print('\n\033[mEsse número foi divisível {} vezes, ele é primo'.format(d))
