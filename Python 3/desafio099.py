# desempacotando valores
from time import sleep

def maior(*num):
    m = 0
    for c in range(0,len(num)):
        print(f'{num[c]}', end = ' ', flush = True)
        sleep(0.5)
        if c == 0:
            m = num[c]
        else:
            if num[c] > m:
                m = num[c]

    print(f'Foram informados {len(num)} números.')
    print(f'O maior número é {m}.')
    print('-='*30)


maior(2, 9, 4, 2, 0, 4, 5)
maior(3, 7, 2, 9)
maior(6)
maior()
maior(12, 3, 2, 32, 11, 0, 9)
