# qual peso é maior
p1 = 0
p2 = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c )))
    if c == 1:
        p1 = peso
        p2 = peso
    else:
        if peso > p1:
            p1 = peso
        if peso < p2:
            p2 = peso
print('O maior peso é {} e o menor é {}'.format(p1, p2))
