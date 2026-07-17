# usando 'break' para quebrar loop infinito
cont = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foi digitado {cont} números e a soma é {soma}')
