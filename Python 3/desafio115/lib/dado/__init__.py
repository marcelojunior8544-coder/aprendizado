from lib.interface import cabecalho
def ArquivoExiste(nome):
    try:
       a = open(nome, 'rt')
       a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro ao criar o arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao ler o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao cadastrar')
        else:
            print(f'Cadastrado de {nome} realizado com sucesso')
    finally:
        a.close()
