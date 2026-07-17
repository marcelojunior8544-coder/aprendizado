# Calcular média e descidir se foi aprovado, se fica na recuperação ou foi reprovado
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2
print('Sua média é de {:.1f}'.format(media))
if media >= 7:
    print('\033[36mVocê foi aprovado!')
elif 7 > media >= 5:
    print('\033[33mVocê precisa fazer recuperação.')
else:
    print('\033[31mVocê foi reprovado.')
