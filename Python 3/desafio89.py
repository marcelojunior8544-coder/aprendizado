# Lista de notas dos alunos
alunos = []

#inserindo dados na lista
while True:
    nome = str(input('Nome: ')).strip().title()
    nota1 = float(input(f'1ª nota de {nome}: '))
    nota2 = float(input(f'2ª nota de {nome}: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

# tabela de nomes e média dos alunos
print('-='*20)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>5}')
print('-'*25)
for c in range(0, len(alunos)):
    print(f'{c:<5} {alunos[c][0]:<10} {alunos[c][2]:>5.1f}')

# mostrando as notas dos alunos
while True:
    n = int(input('Quer mostrar a nota de qual aluno? (999 para parar): '))
    print('-'*25)
    if n == 999:
        print('FINALIZANDO...')
        break
    if 0 <= n < len(alunos):
        print(f'Notas de {alunos[n][0]} são {alunos[n][1]}')
    else:
        print(f'Não existe aluno com o número {n}. Tente novamente.')
print('-'*25)
