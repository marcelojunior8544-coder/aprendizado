r = float(input('Digite o valor em Reais: '))
d = r / 5.15
e = r / 5.91
print('Com R${:.2f} pode comprar US${:.2f} e €{:.2f}'.format(r,d,e))
