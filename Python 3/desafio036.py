# Calcular um financiamento de uma casa
vc = float(input('Quanto é a casa: R$'))
salario = float(input('Qual é o seu salário: R$'))
anos = int(input('Em quantos anos deseja pagar: '))
parcela = vc / (anos * 12)
#print('Para comprar uma casa de R${:.2f} em {}'.format(vc,anos))
#print('a prestação será de R${:.2f}'.format(parcela))
if parcela > salario * 30 / 100:
    print('A parcela excede o limite de salário')
else:
    print('O finaciamento foi aprovado e o valor da parcela dessa casa fica por R${:.2f}'.format(parcela))
