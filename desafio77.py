# dizer vogais de cada palavra em uma tupla
palavras = ('Arroz', 'Parede', 'Carro', 'Violao', 'Carne', 'Legumes', 'Pateta',
            'Pneumoultramicroscopicossilicovolcanoconiotico')
for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end=' ')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra.lower(), end=' ')
print('\nAcabou')
