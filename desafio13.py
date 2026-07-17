sa = float(input('Salário antes do reajuste: R$'))
sn = sa+(sa*15/100)
print('O salário antes do aumento é R${:.2f} e o novo salário depois do aumento de 15% ficará por R${:.2f}'.format(sa,sn))
