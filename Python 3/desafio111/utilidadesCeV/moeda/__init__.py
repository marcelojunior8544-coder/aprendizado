def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def metade(v, f= False):
    res = v / 2
    return res if not f else moeda(res)


def dobro(v, f= False):
    res = v * 2
    return res if not f else moeda(res)


def aumentar(v, p, f=False):
    res = v + (v * p / 100)
    return res if not f else moeda(res)


def diminuir(v, p, f=False):
    res = v - (v * p / 100)
    return res if not f else moeda(res)


def resumo(v=0, a=10, d=5):
    print('-'*30)
    print(f'{"RESUMO DO VALOR".center(30)}')
    print('-'*30)
    print(f'{"Preço analisado:":18} {moeda(v)}')
    print(f'{"Dobro do preço:":18} {dobro(v, True)}')
    print(f'{"Metade do preço:":18} {metade(v, True)}')
    print(f'{f"{a}% de aumento:":18} {aumentar(v,a, True)}')
    print(f"{f'{d}% de redução:':18} {diminuir(v,d, True)}")
    print('-'*30)
