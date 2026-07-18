angulo = float(input('Digite o valor do angulo: '))
from math import radians,sin, cos ,tan
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {} tem:\n'
      'O seno de {:.2f}.\n'
      'O cosseno de {:.2f}.\n'
      'A tangente de {:.2f}.'
      .format(angulo,seno,cosseno,tangente))
