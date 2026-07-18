from random import randint
num = randint(0,5) # Sorteia um número
print('-='*20)
print('Vou sortear um número de 0 a 5')
print('-='*20)
jogador = int(input('Pensei em um número, tente adivinhar. ')) # Jogador tenta adivinhar
if jogador == num:
    print('Parabés! Você ganhou!')
else:
    print('Que azar. O número era {}\n'
          'Mais sorte na próxina.'.format(num))
