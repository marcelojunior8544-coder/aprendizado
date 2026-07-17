# Definir catecoria de competição
from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc # Calculo de idade

# Decidindo a categoria
if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Junior'
elif idade <= 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print('Vai competir na categoria {}.'.format(categoria))
