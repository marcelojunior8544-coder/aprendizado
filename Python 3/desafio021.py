# Reproduzir mp3
import pygame # Python 3.11 ou anterior

pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
