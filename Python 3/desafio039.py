# Informar se tá na hora de se alistar
from datetime import date
sexo = str(input('Qual seu ? [M / F] ').strip().upper())
nasc = int(input('Diga o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if sexo == 'M':
    if idade < 18:
        saldo = 18 - idade
        if saldo > 1:
            print('Você vai precisar se alistar em {} anos'.format(saldo))
            ano = atual - saldo
            print('Seu alistamento será em {} anos.'.format(ano))
        else:
            print('Você vai precisar se alistar ano que vem')
    elif idade == 18:
        print('Está na hora de se alistar.')
    else:
        saldo = idade - 18
        if saldo > 1:
            print('Já passou {} anos da época do alistamento'.format(saldo))
            ano = atual - saldo
            print('Seu alistamento foi em {}.'.format(ano))
        else:
            print('Seu alistamento foi ano passado.')
elif sexo == 'F':
    print('Mulheres não precisam se alistar obrigatoriamente.')
