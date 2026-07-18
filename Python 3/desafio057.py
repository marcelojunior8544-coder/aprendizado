# só aceitar digitação correta
sexo = str(input('Digite o sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    print('Sexo invalido')
    sexo = str(input('Digite o sexo [M/F]: ').strip().upper()[0])
print('Fim')