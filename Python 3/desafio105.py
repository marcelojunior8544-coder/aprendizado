# Notas e situação de uma turma
def notas(*n, sit=False):
    """
    ->Função para analisar notas de vário alunos
    :param n: uma ou mais notas dos alunos
    :param sit: [opcional] indicar a situação da turma
    :return: dicionário com informações da turma
    """
    result = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n) / len(n)}
    if sit:
        if result['média'] >= 7:
            result['situação'] = 'Boa'
        elif result['média'] >= 6:
            result['situação'] = 'Razoável'
        else:
            result['situação'] = 'Ruim'
    return result


resp = (notas(6, 7, 5, 6, sit=True))
print(resp)