# sequencia de fibonacci
print('-='*20)
print('{:^50}'.format('Sequência de Fibonacci'))
print('-='*20)
num = int(input('Quantos termos deseja mostrar? '))
v1 = 0
v2 = 1
c = 3
print('~'*20)
print('{} -> {}'.format(v1, v2), end=' ')
while c <=num:
    v3 = v1 + v2
    print('->{}'.format(v3), end=' ')
    v1 = v2
    v2 = v3
    c += 1
print('->Fim')
print('~'*20)
