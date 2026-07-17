# calculando fatorial com 'for'
n = int(input('Digite um número para calcular o fatorial: '))
f = 1
print('{}! ='.format(n),end=' ')
for c in range(n, 0, -1):
    print(c, end = ' ')
    print('x' if c > 1 else '=', end = ' ')
    f *= n
    n -= 1
print(f)
