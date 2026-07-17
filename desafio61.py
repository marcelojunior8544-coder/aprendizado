# Progressão aritmética v2
print('=-'*15)
print('{:^30}'.format('Gerador de PA.'))
print('=-'*15)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão'))
d = 1
while d <= 10:
    print('{}'.format(n), end=' ')
    d += 1
    n += r
    print('->' if d <= 10 else ' ', end=' ')
print('\nFIM')
