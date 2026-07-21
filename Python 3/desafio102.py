# função do fatorial e escolher se mostra o calculo ou não

def fatorial(n=1, show=False):
    """
    -> Calcula o fatorial de um numero.
    :param n: O número a ser calculado.
    :param show: [opcional] Mostrar ou não a conta.
    :return:
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c}', end=' x ')
            else:
                print(f'{c}', end=' = ')
    return f

print(fatorial(6, True))
print(fatorial(5, True))
