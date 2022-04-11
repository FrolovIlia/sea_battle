import pygame
from pygame.locals import *
from GameLogic import dead_ships

display_size_x = 840
display_size_y = 600

small_xy_hit_size = display_size_y / 30
ship_size = (display_size_x / 14, display_size_y / 3)

pygame.init()
game_display = pygame.display.set_mode((display_size_x, display_size_y))
pygame.display.set_caption('BattleShip')
pygame.display.set_icon(pygame.image.load("pictures/ship_icon.png"))
game_display.fill('white')

# Параметры счётчика
hit_counter_1 = pygame.font.Font(None, 36)

sign_counter = hit_counter_1.render(f'{dead_ships}', True, (180, 0, 0))
game_display.blit(sign_counter, (85, 20))

player_name = hit_counter_1.render('Player 1', True, (180, 0, 0))
game_display.blit(player_name, (50, 50))

# Параметры кораблей и вспомогательных элементов

carrier_shape = pygame.transform.scale(pygame.image.load('pictures/Carrier_shape.png'), (120, 30))
game_display.blit(carrier_shape, ship_size)

empty_cell = pygame.transform.scale(pygame.image.load('pictures/m_Hit small.png'), (small_xy_hit_size, small_xy_hit_size))
game_display.blit(empty_cell, (180, display_size_y / 3))

padded_cell = pygame.transform.scale(pygame.image.load('pictures/m_Miss small.png'), (small_xy_hit_size, small_xy_hit_size))
game_display.blit(padded_cell, (200, display_size_y / 3))






def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()


while True:
    event_handler()
    pygame.display.update()
