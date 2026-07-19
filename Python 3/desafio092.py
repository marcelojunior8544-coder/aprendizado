# calcular tempo até se aposentar
from datetime import datetime
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip().title()
pessoa['idade'] = datetime.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho: '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Qual o ano de contratação: '))
    pessoa['salário'] = float(input('Qual o valor do salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + 35 - (datetime.today().year - pessoa['contratação'])
print('-='*30)
for k , v in pessoa.items():
    print(f'{k} tem o valor {v}')
