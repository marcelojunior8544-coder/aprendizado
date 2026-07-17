# 10 resultados de uma progressão aritmética
print('='*30)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('='*30)
n = int(input('Digite o primeiro termo: '))
r = int(input('Qual é a razão da PA: '))
d = n + (10 -1 )*r
for c in range(n, d + r, r):
    print('{}'.format(c), end=' ')
print('Fim')