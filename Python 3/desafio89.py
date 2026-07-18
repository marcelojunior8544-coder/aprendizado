# Lista de notas dos alunos
alunos = []

#inserindo dados na lista
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().title()
    nota1 = float(input(f'Digite a 1ª nota de {nome}: '))
    nota2 = float(input(f'Digite a 2ª nota de {nome}: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

# tabela de nomes e média dos alunos
print('-='*30)
print('{:<5}{:<10}{:^5}'.format('No.', 'NOME', 'MÉDIA'))
print('-'*30)
for c in range(0, len(alunos)):
    print(f'{c:<5} {alunos[c][0]:<10} {alunos[c][2]:^5.1f}')
print('-'*30)

# mostrando as notas dos alunos
while True:
    n = int(input('Quer mostrar a nota de qual aluno? (999 para parar): '))
    if n == 999:
        print('FINALIZANDO...')
        break
    else:
        print(f'Notas de {alunos[n][0]} são {alunos[n][1]}')
print('-'*30)
