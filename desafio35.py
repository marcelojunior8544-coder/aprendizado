print('-='*15)
print('\033[1:34mAnalisando Triângulos\033[m')
print('-='*15)
a = int(input('Digite o valor da primeira linha: '))
b = int(input('Digite o valor da segunda linha: '))
c = int(input('Digite o valor da terceira linha: '))
if a + b > c and a + c > b and b + c > a:
    print('Essas 3 linhas \033[32mPODEM FORMAR\033[m um triângulo.')
else:
    print('Essas 3 linhas \033[31mNÃO PODEM FORMAR\033[m um triângulo.')
