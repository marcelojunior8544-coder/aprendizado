# progressão aritmética v3
# from time import sleep
num = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
d = 1
n = num
c = 0
t = 0
m = 10
while m != 0:
    t = t + m
    while d <= t:
        print('{}'.format(n), end=' ')
        d += 1
        n += r
        c += 1
        print('->' if d <= t else ' ', end=' ')
    print('\nPAUSA')
    m = int(input('Quantos termos deseja mostrar a mais? '))
print('\nForam mostrados {} termos.'.format(c))
