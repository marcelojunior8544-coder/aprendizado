# iniciando construção de menus
from time import sleep
op = 0
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
while op != 5:
    print('='*35)
    op = int(input('''Escolha qual operação fazer com os números.
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa.'''))
    if op == 1:
        r = num1 + num2
        print('{} + {} = {}'.format(num1, num2, r))
        sleep(0.5)
    elif op == 2:
        r = num1 * num2
        print('{} * {} = {}'.format(num1, num2, r))
        sleep(0.5)
    elif op == 3:
        if num1 > num2:
            print('{} > {}'.format(num1, num2))
            sleep(0.5)
        else:
            print('{} > {}'.format(num2 , num1))
            sleep(0.5)
    elif op == 4:
        num1 = int(input('Digite novo valor: '))
        num2 = int(input('Digite novo valor; '))
    elif op == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Digite uma opção válida.')
print('Fim do programa')
