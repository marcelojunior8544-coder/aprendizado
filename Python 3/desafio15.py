dias = int(input('Alugado por quantos dias? '))
km = float(input('Quantos km rodados? '))
v1 = dias * 60
v2 = km * 0.15
v3 = v1 +v2
print('O valor do aluguel ficou em R${:.2f} pelos dias, R${} pelos km e R${} ao total.'.format(v1,v2,v3))
