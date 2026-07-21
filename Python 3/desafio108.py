from desafio108 import moeda
v = float(input('Digite o valor: R$'))
print(f'A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}.')
print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}.')
print(f'Aumentando 10% fica {moeda.moeda(moeda.aumentar(v, 10))}')