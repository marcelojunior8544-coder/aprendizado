# Verificar se é palindromo
frase = str(input('Digite uma frase: ').strip().lower())
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''inverso = ' '
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('é um palindromo')
else:
    print('não é um palindromo')
