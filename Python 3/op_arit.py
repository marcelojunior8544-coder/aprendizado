# A ordem de precedencia é primeiro os (), segundo os **, terceiro os * / // % (na ordem q aparecer) e por ultimo os: + e -

n1 = int(input('Primeiro valor '))
n2 = int(input('Segundo valor '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s,m, d), end=" ")
print('A divisão inteira é {} e a potência é {}'.format(di,e))
