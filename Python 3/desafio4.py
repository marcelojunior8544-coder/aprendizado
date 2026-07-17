x = str(input('digite algo ')).strip()
print(type(x),'\n',
      x.isnumeric(),'\n', # Teste se está escrito apenas com números
      x.isalpha(),'\n', # Teste se está escrito apenas com letras
      x.isalnum(),'\n', # Teste se é possui algarismos Alfanumericos
      x.isdigit(),'\n', # Teste se é número decimal
      x.isupper(),'\n', # Teste se está escrito apenas em maiusculas
      x.islower()) # Teste se está escrito apenas em minusculas
