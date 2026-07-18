# somar apenas números pares
s = 0
p = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        s += n
        p += 1
if p == 1:
    print('O único número par é {}'.format(s))
elif p > 1:
    print('A soma dos {} números pares é de {}'.format(p, s))
else:
    print('Nem um número par informado')
    