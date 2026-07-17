cidade = str(input('Digite o nome da cidade: ')).strip()
if 'santo' in cidade[:5].lower():
    print('Essa cidade começa com Santo')
else:
    print('Essa cidade não começa com Santo')
