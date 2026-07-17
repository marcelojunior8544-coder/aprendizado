# inserir valores entre valores já existentes
lista = []
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0:
        lista.append(num)
        print('O valor foi inserido no final')
    else:
        for p, v in enumerate(lista):
            if num <= v:
                lista.insert(p, num)
                print(f'O valor foi inserido na posição {p}')
                break
        else:
            lista.append(num)
            print('O valor foi inserido no final')
print('-=' * 30)
print(f'Os valores em ordem foram: {lista}')
