# print com comprimento adaptável.

def escreva(txt):
    tam = len(txt)+4
    print('~'*tam)
    print(f'  {txt}')
    print('~'*tam)


escreva('É hora do show')
escreva('Sai de casa comi pra caralho')
escreva('BIRL')
