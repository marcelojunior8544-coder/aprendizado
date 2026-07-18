# calcular fatorial
num = int(input('Digite um número: '))
f = 1
n = num
print ('{}! ='.format(num),end = ' ')
while n > 0:
    print('{}'.format(n),end = ' ')
    print('x' if n > 1 else '=', end = ' ')
    f *= n
    n -= 1
print('{}'.format(f))
