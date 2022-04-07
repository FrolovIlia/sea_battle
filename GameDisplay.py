import pygame
from pygame.locals import *

pygame.init()
game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('BattleShip game')

game_display.fill('white')
# img = pygame.image.load('img1.png')
# game_display.blit(img, (0, 0))


def event_handler():
    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit()
            quit()


while True:
    event_handler()
    pygame.display.update()



