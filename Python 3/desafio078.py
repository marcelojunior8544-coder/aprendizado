# Preencher uma lista e verificar maior e menor valor em uma lista
lista = []
# Preenchendo a lista
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
# Definindo o maior e menor valor na lista
maior = max(lista)
menor = min(lista)
print('-=' * 20)
print(f'Voce digitou os valores {lista}')
print('-=' * 20)
# Indicando as posições dos valores
print(f'O maior valor digitado foi {maior} nas posições: ', end=' ')
for p , v in enumerate(lista):
    if v == maior:
        print(f'{p}...', end=' ')
    print()
print('-=' * 20)
print(f'O menor valor digitado foi {menor} nas posições: ', end=' ')
for p , v in enumerate(lista):
    if v == menor:
        print(f'{p}...', end=' ')
    print()
print('-=' * 20)
