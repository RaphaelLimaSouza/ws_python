import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
x = largura/2
y = 0

cor_fundo = (0, 0, 0) #variavel cor do fundo


tela = pygame.display.set_mode((largura, altura), pygame.DOUBLEBUF) #Primeiro, você precisa adicionar o parâmetro pygame.DOUBLEBUF na função pygame.display.set_mode(), que habilita o double buffering na superfície tela.
pygame.display.set_caption('Jogo do Grupo Nota 10')
relogio = pygame.time.Clock()

while True:
    relogio.tick(10)
    #tela.fill((0, 0, 0))  - esse tela.fill sai daqui
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        tela.fill((0, 0, 0))
        pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
        if y >= altura:
            y = 0
        y = y + 10
        print(y)

    pygame.display.flip() #Segundo, você precisa substituir a função pygame.display.update() pela função pygame.display.flip()
