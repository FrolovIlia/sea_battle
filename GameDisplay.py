import pygame
from pygame.locals import *

display_size_x = 840
display_size_y = 600

pygame.init()
game_display = pygame.display.set_mode((display_size_x, display_size_y))
pygame.display.set_caption('BattleShip')
pygame.display.set_icon(pygame.image.load("pictures/ship_icon.png"))
game_display.fill('white')

aircraft_shape = pygame.transform.scale(pygame.image.load('pictures/Aircraft Shape.png'), (90, 30))
game_display.blit(aircraft_shape, (50, 100))

empty_cell = pygame.transform.scale(pygame.image.load('pictures/m_Hit small.png'), (20, 20))
game_display.blit(empty_cell, (140, 110))

padded_cell = pygame.transform.scale(pygame.image.load('pictures/m_Miss small.png'), (20, 20))
game_display.blit(padded_cell, (160, 110))


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()


while True:
    event_handler()
    pygame.display.update()
