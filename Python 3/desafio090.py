# iniciando trabalhos com dicionário
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} = {v}')
