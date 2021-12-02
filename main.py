import math
import random
import pygame
import sys
import graphicsLibrary

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()



while True:
    extension=(1080,720)
    screen.fill("white")


    border2 = graphicsLibrary.draw(screen, [[200,200], [300, 300]],(250,65,88), borderFull=51, borderColor=(12,0,14), transparency=0 )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(60)
