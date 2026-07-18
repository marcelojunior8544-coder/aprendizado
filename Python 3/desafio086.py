# criando um matriz
matriz = [[], [] , []]

# inserindo os valores na matriz
for l in range(0, 3):
    for c in range(0, 3):
     matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

# mostrando a matriz
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]', end = ' ')
    print()
