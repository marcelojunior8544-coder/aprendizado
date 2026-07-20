# Verificando se é um número inteiro

def leiaint(msg):
    """
    ->Função que só avança se for digitado um número inteiro
    :param msg: entrada do valor a ser verificado
    :return: o numero inteiro
    """
    
    valor = 0
    ok = False

    while True:
        num = input(msg)
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('\033[31mErro! Digite um número inteiro.\033[m')
        if ok:
            break
    return valor


# programa principal
n = leiaint('Digite um número: ')
print(f'O valor digitado foi {n}')
