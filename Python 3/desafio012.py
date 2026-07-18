v = float(input('Valor do produto: R$'))
vf = v - (v*5/100)
print('Um produto de R${:.2f} depois do desconto de 5% fica por R${:.2f}'.format(v,vf))
