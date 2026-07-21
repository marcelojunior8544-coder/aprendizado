# modulo para trabalhar com valores de moeda
from desafio107 import moeda

n = float(input('Digite um valor: R$'))
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(n, 10)}')
print(f'Diminuindo 13%, temos R${moeda.diminuir(n, 13)}')