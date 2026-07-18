s = 0
c = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        s += n
        c =+ 1
print('A soma dos {} números ímpares multiplos de 3 de 1 à 500 é {}.'.format(c, s))
