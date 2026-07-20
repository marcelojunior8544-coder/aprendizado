# começando a trabalhar com funções
def área(c, l):
    a = c * l
    print(f'A área de um terreno {c:.2f}m x {l:.2f}m é de {a:.2f}m²')

print('-'*30)
print('Trabalhando a área')
área(
    c = float(input('Valor do comprimento: ')),
    l = float(input('Valor da largura: '))
)