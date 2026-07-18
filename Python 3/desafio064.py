# somar números exeto a flag 999
num = int(input('Digite um número ou digite 999 para parar.: '))
quantidade= soma = 0
while num != 999:
    soma += num
    quantidade += 1
    num = int(input('Digite um número ou digite 999 para parar.: '))
print('Foram digitados {} números.'.format(quantidade))
print('A soma desses números é {}.'.format(soma))