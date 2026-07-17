#manipulação de tupla
tupla = tuple(int(input('Digite um número').strip())for i in range(0,4))
print('Você digitou os valores:', end =' ')
for n in tupla:
    print(n, end=' ')
print(f'\nFoi digitado {tupla.count(9)} números 9.')
if 3 in tupla:
    print(f'O primeiro número 3 aparece na {tupla.index(3)+1}ª posição.')
else:
    print('Não tem número 3.')
print('Os valores pares digitados foram: ', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
