n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1 > n2:
    print('O {} é {}MAIOR{}'.format(n1,'\033[1:31m','\033[m'))
elif n2 > n1:
    print('O {} é {}MAIOR{}'.format(n2,'\033[1:31m','\033[m'))
else:
    print('O valores são {}IGUAIS{}'.format('\033[1:34m','\033[m'))
