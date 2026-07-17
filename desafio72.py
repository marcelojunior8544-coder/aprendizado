# escrever números por extenso
contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'quatorze',
            'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')
num = 0
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    while not 0<= num <= 20:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Você digitou o numero {contagem[num]}.')
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'N':
        break
