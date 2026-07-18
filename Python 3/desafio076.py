# lista de preços
lista = ('Pão', 2.50,
         'Leite', 2.00,
         'Lápis', 1.50,
         'Borracha', 1.00,
         'Notebook', 3000,
         'Chiclete', 2.5,
         'Refrigerante', 3.00)
print('-'*50)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:-<30}R$',end=' ')
    else:
        print(f'{lista[pos]:>8.2f}')
print('-'*50)
