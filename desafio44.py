# Calculadora de preço dependendo do modo de pagamento
valor = float(input('Digite o valor da compra: R$'))
print('''Diga o modo de pagamento:
[ 1 ] à vista (dinheiro/cheque)
[ 2 ] à vista (cartão)
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
modo = int(input('Qual é a opção?'))
if modo == 1:
    novo = valor - (valor * 10 /100)
elif modo == 2:
    novo = valor - (valor * 5 / 100)
elif modo == 3:
    novo = valor
    parcela = novo / 2
    print('Esse pagamento fica duas parcelas de R${:.2f} sem juros.'.format(parcela))
elif modo == 4:
    novo = valor + (valor * 20 / 100)
    x = int(input('Em quantas vezes deseja pagar: '))
    parcela = novo / x
    print('Esse pagamento fica {} parcelas de R${:.2f} com juros.'.format( x, parcela))
else:
    novo = 0
    print('{}{}{}'.format('\033[1:31m','NÃO FOI INSERIDO UM MODO VÁLIDO DE PAGAMENTO.','\033[m'))
print('O pagamento total fica em R${:.2f}'.format(novo))
