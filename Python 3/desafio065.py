# ler varios numeros e calcular a media deles e qual maior e menor
cont = soma = media  = maior = menor = 0
resp ='S'
while resp != 'N':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp not in 'SN':
        print('Resposta invalida!')
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    soma += num
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num
print('Foram digitados {} números e a média deles é {:.2f}'.format(cont, media))
print('{} é o maior e {} é o menor'.format(maior, menor))
