from lib.interface import*
from lib.dado import*
from time import sleep

arq = 'lista.txt'
if not ArquivoExiste(arq):
    CriarArquivo(arq)
while True:
    resp = menu(['Ver lista','Cadastrar Pessoa', 'Sair do sistema'])
    if resp == 1:
        # mostrar o conteudo do arquivo
        LerArquivo(arq)
    elif resp == 2:
        # cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema')
        break
    else:
        print(f'{cor[1]}ERRO! Digite uma opção válida!{cor[0]}')
    sleep(2)
