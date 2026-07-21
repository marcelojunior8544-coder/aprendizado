#
def ficha(jogador='', gols=''):
    """
    -> Função para ficha de jogador
    :param jogador: Nome do jogador
    :param gols: número de gols
    :return: ficha do jogador
    """
    if not jogador.isalpha():
        jogador = '<desconhecido>'
    if not gols.isnumeric():
        gols = 0
    else:
        gols = int(gols)
    print(f'O jogador {jogador} fez {gols} gols')


print('=-'*15)
nome = str(input('Digite o nome do jogador: '))
gol = str(input('Número de gols: '))
ficha(nome, gol)