dia = int(input ('Dia = '))
mês = str(input ('Mês = ')).strip().title()
ano = int(input ('Ano = '))
print ('Você nasceu em \033[4:32m{}/{}/{}\033[m. Correto?'.format(dia,mês,ano))
