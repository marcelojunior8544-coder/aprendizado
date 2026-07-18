# trabalhando tuplas
time = ('Palmeiras', 'Flamengo', 'Fluminense','Athletico-PR', 'Red Bull Bragantino',
        'Bahia', 'Coritiba', 'São Paulo', 'Atlético-MG', 'Corinthians', 'Cruzeiro',
        'Botafogo', 'Vitória', 'Internacional', 'Santos', 'Grêmio', 'Vasco', 'Remo',
        'Mirassol', 'Chapecoense')
print('-'*40)
print(time)
print('-'*40)
print(f'Os cinco primeiros são {time[:5]}')
print('-'*40)
print(f'Os quatro ultimos são {time[-4:]}')
print('-'*40)
print(sorted(time))
print('-'*40)
print(f'O time da Chapecoense está na {time.index("Chapecoense")+1}ª posição.')
print('-'*40)
