# função contador
from time import sleep

def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    p_abs = abs(p)
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)

    if f < i:
        p_real = -p_abs
        f_real = f - 1
    else:
        p_real = p_abs
        f_real = f + 1

    for c in range(i, f_real, p_real):
        print(c, end = ' ', flush = True)
        sleep(0.5)
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)

print('Contagem personalizada.')
contador(
    int(input('Início: ')),
    int(input('Fim: ')),
    int(input('Passo: '))
)
print('-='*20)
