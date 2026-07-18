# estatísticas de produtos
cont = totg = menor = pm = 0
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Valor do produto: R$'))
    cont += 1
    totg += valor

    # Verificando o mais barato
    nome = ' '
    if cont == 1 or valor < menor:
        nome = produto
        menor = valor
    
    # contando os produtos que custam mais de R$1000
    if valor > 1000:
        pm += 1

    t = ' '
    while t not in 'SN': # garantindo resposta válida
        t = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if t == 'N':
        break

print(f'O total da compra foi R${totg:.2f}')
print(f'O produto mais barato é {nome}, custamdo R${menor:.2f}')
print(f'{pm} produtos custam mais de R$1000,00')
