#
c = ('\033[m',       #0 = limpa
   '\033[0;30;41m',#1 = vermelho
   '\033[0;30;44m',#2 = azul
   '\033[0;30;43m',#3 = amarelo
   '\033[0;30;42m'

   )

def ajuda(msg):
    while True:
        titulo('SISTEMA DE AJUDA PYTHON', 4)
        comando = str(input(msg))
        if comando.upper() == 'FIM':
            titulo('Até Logo!', 1)
            break
        else:
            titulo(f"Acessando o manual do comando '{comando}'", 2)
            print(c[3], end = '')
            help(comando)
            print(c[0], end = '')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end = '')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end = '')


ajuda('Função ou Biblioteca > ')
