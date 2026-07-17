# Verificação de infomações de pessoas
sid = 0
i = 0
n = ''
m = 0
for c in range(1, 5):
    print('-'*5,'{}ª PESSOA'.format(c),'-'*5)
    sexo = str(input('Sexo [M/F]: ').strip().upper()[0])
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sid += idade
    if c == 1 and sexo == 'M':
        i = idade
        n = nome
    if idade > i and sexo == 'M':
        i = idade
        n = nome
    if sexo == 'F' and idade < 20:
        m += 1
media = sid / 4
print('O homen mais velho tem {} anos e se chama {}.'.format(i, n))
print('A média de idade de todos é de {:.2f}.'.format(media))
print('Tem {} mulheres menores de 20 anos'.format(m))
