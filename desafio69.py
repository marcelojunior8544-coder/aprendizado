# gerenciamento de pessoas
maiores = mul20 = hom = 0

while True:
    print('-'*30)
    print('Cadastre uma pessoa')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': # Garantir resposta válida
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    #Contagem de pessoas
    if sexo =='M':
        hom += 1
    if sexo == 'F' and idade < 20:
        mul20 += 1
    if idade >= 18:
        maiores += 1

    print('-'*30)

    continuar = ' '
    while continuar not in 'SN': # Garantir resposta válida
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print('-'*30)

if maiores > 1: # Pessoas maiores de 18 anos
    print(f'Foram cadastrados {maiores} maiores de 18 anos. ')
elif maiores == 0:
    print('Não foi cadastrado maiores de 18 anos.')
else:
    print(f'Foi cadastrado {maiores} maior de 18 anos')

if mul20 > 1: # Mulheres menores de 20 anos
    print(f'Foram cadastradas {mul20} mulheres com menos de 20 anos.' )
elif mul20 == 0:
    print('Não foi cadastrada mulher com menos de 20 anos.')
else:
    print(f'Foi cadastrada {mul20} mulher com menos de 20 anos.')

if hom > 1: # Homens cadastrados
    print(f'Foram cadastrados {hom} homens.')
elif hom == 0:
    print('Não foi cadastrado homem.')
else:
    print(f'Foi cadastrado {hom} homem')

print('-'*30)
