# Caixa eletrônico
print('='*25)
print('{:^40}'.format('Banco GuliraX'))
print('='*25)
valor =int(input('Qual o valor vai ser sacado? R$'))
cedula = 50
totcedula = 0
while True:
    if valor >= cedula:
        valor -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de cedulas de R${cedula} é de {totcedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if valor == 0:
            break
print('='*25)
