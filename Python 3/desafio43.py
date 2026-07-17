# Calculadora de IMC
peso = float(input('Digite o seu peso em quilos: ').strip())
altura = float(input('Digite a sua altura em metros: ').strip())
IMC = peso / (altura ** 2)
print('Seu IMC é de {:.1f}.'.format(IMC))
if IMC < 18.5:
    print('Voce está abaixo do peso ideal.')
elif IMC < 25:
    print('Você está na faixa de peso ideal.')
elif IMC < 30:
    print('Você está acima do peso ideal.')
elif IMC < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida')
