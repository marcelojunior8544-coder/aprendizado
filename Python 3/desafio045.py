# Jokenpô
print('-='*20,'\n','Bem vindo ao jogo de Jokenpô','\n','-='*20)
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int((input('''Escolha Pedra, Papel ou Tesoura:
 [ 0 ] Pedra
 [ 1 ] Papel
 [ 2 ] Tesoura: ''')))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
print('-='*20)
print('Eu escolhi {}'.format(itens[computador]))
if computador == 0: # computador jogou pedra
    if jogador == 0: # pedra
        print('Você escolheu {}.'.format(itens[jogador]))
        print('Nós empatamos')
    elif jogador == 1: # papel
        print('Voce escolheu {}.'.format(itens[jogador]))
        print('Você ganhou! Parabéns!')
    elif jogador == 2: # tesoura
        print('Você escolheu {}.'.format(itens[jogador]))
        print('Eu ganhei! Mais sorte na próxima.')
    else:
        print('Jogada invalida')

elif computador == 1: # computador jogou papel
    if jogador == 0: # pedra
        print('Você escolheu {}.'.format(itens[jogador]))
        print('Eu ganhei! Mais sorte na próxima.')
    elif jogador ==1: #papel
        print('Você escolheu {}.'.format(itens[jogador]))
        print('Nós empatamos')
    elif jogador == 2: #tesoura
        print('Você escolheu {}.'.format(itens[jogador]))
        print('Voce ganhou! Parabéns!')
    else:
        print('Jogada invalida.')

elif computador == 2: # computador jogou tesoura
    if jogador == 0: # pedra
        print('Você escolheu {}.'.format(itens[jogador]))
        print('Você ganhou! Parabéns!')
    elif jogador == 1: # papel
        print('Você escolheu {}.'.format(itens[jogador]))
        print('Eu ganhei! Mais sorte na próxima')
    elif jogador == 2: #tesoura
        print('Você escolheu {}.'.format(itens[jogador]))
        print('Nós empatamos')
    else:
        print('Jogada invalida.')
print('-='*20)
