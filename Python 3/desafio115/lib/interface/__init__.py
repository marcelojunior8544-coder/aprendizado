cor=('\033[m',  #0 = limpa
     '\033[31m',#1 = vermelho
     '\033[33m',#2 = amarelo
     '\033[34m')#3 = azul
def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def leiaint(msg):
    while True:
        try:
            valor = int(input(msg).strip())
        except ValueError or TypeError:
            print(f'{cor[1]}Digite um número inteiro{cor[0]}')
            continue
        except KeyboardInterrupt:
            print(f'\n{cor[1]}O usuário preferiu não digitar esse valor{cor[0]}')
            return 0
        else:
            return valor


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cor[2]}{c}{cor[0]} - {cor[3]}{item}{cor[0]}')
        c += 1
    print(linha())
    opc = leiaint(f'{cor[2]}Sua opção: {cor[0]}')
    return opc
