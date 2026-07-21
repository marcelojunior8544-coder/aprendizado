def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def metade(v, f= False):
    if f:
        res = moeda(v / 2)
    else:
        res = v / 2
    return res


def dobro(v, f= False):
    if f:
        res = moeda(v * 2)
    else:
        res = v * 2
    return res


def aumentar(v, p, f=False):
    if f:
        res = moeda(v + (v * p / 100))
    else:
        res = v + (v * p / 100)
    return res


def diminuir(v, p, f=False):
    if f:
        res = moeda(v - (v * p / 100))
    else:
        res = v - (v * p / 100)
    return res

