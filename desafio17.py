import math
co = float(input('Digite o valor do cateto oposto '))
ca = float(input('Digite o valor do cateto adjacente '))
hipo = math.hypot(co,ca)
print('Um triângulo com o cateto oposto de {}'
      ' e cateto adjacente de {},'
      'tem a hipotenusa de {:.2f}'.format(co,ca,hipo)
      )