# Verificar se uma expressão está com os parênteses fechados corretamente
expr = str(input('Digite uma expressão: ')).strip()
pilha = []

for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão é válida.')
else:
    print('Expressão inválida.')
