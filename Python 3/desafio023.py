num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número {} tem \n'
      'Unidade {}\n'
      'Dezena {} \n'
      'Centena {} \n'
      'Milhar {}.'
      .format(num,u,d,c,m))
