# desempacotando números

def maior(*num):
    m = 0
    for c in range(0,len(num)):
        if c == 0:
            m = num[c]
        else:
            if num[c] > m:
                m = num[c]

    print('-='*40)
    print(f'{num} Foram informados {len(num)} números.')
    print(f'O maior número é {m}.')
    print('-='*40)


maior(2, 9, 4, 2, 0, 4, 5)
