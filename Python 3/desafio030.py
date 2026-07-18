num = int(input('Digite um número: '))
if num % 2 == 0:
    print('Esse número é \033[4;35mPar\033[m.')
else:
    print('Esse número é \033[4;31mÍMPAR\033[m.')