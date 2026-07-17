# Analise de triângulo v2
l1 = float(input('Digite o primeiro lado: ').strip())
l2 = float(input('Digite o segundo lado: ').strip())
l3 = float(input('Digite o terceiro lado: ').strip())
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Esses valores formam um triângulo ', end='')
    if  l1 == l2  == l3:
        print('EQUILÁTERO.')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Esses Valores não formam um TRIÂNGULO.')
    