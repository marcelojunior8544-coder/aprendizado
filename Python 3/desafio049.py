# Tabuada V2
n = int(input('Digite um número inteiro para ver sua tabuada: '))
print('-='*15)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, c * n))
print('-='*15)
