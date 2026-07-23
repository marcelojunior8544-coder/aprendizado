# melhorando função leiaint e criando a função leiafloat

def leiaint(msg):
    while True:
        try:
            valor = int(input(msg).strip())
        except ValueError or TypeError:
            print(f'\033[31mValor inválido, tente novamente\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse valor\033[m')
            return 0
        else:
            return valor


def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg).strip())
        except ValueError or TypeError:
            print(f'\033[31mValor invalido, tente novamente\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse valor\033[m')
            return 0
        else:
            return valor


inteiro=leiaint('Digite um numero inteiro: ')
real=leiafloat('Digite um numero real: ')
print(f'O valor inteiro é {inteiro} e o valor real é {real}')
