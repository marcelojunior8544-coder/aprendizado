# verificar quantas pessoas maior de 21
from datetime import date
atual = date.today().year
p = 0
n = 0
for c in range(1, 8):
    nasc = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - nasc
    if idade >= 21:
        p += 1
    else:
        n += 1
print('{} maior de idade e {} menor de idade'.format(p, n))