vel = float(input('Qual é a velocidade em km/h? '))
if vel > 80:
    print('Você excedeu o ilimite de  velocidade e foi multado em R${:.2f}.'
          .format((vel - 80)*7))
print('Tenha uma boa viagem.')
