import pygame
from pygame.locals import *
from GameLogic import dead_ships

display_size_x = 840
display_size_y = 600
space = 4

small_xy_hit_size = display_size_y / 30
ship_size = (display_size_x / 14, display_size_y / 3)

pygame.init()
game_display = pygame.display.set_mode((display_size_x, display_size_y))
pygame.display.set_caption('BattleShip')
pygame.display.set_icon(pygame.image.load("pictures/ship_icon.png"))
game_display.fill('white')

# Параметры счётчика
pygame.draw.rect(game_display, (250, 203, 3),
                 (display_size_x / 14, display_size_y / 10, display_size_x / 7, display_size_x / 7))

hit_counter_1 = pygame.font.Font(None, 36)

sign_counter = hit_counter_1.render(f'{dead_ships}', True, (180, 0, 0))
game_display.blit(sign_counter, (115, 80))

player_name = hit_counter_1.render('Player 1', True, (180, 0, 0))
game_display.blit(player_name, (75, 140))

pygame.draw.line(game_display, 'black', [70, 120], [170, 120], 2)

# Параметры кораблей и вспомогательных элементов
carrier_shape = pygame.transform.scale(pygame.image.load('pictures/Carrier_shape.png'), (120, 30))
game_display.blit(carrier_shape, ship_size)

# empty_cell = pygame.transform.scale(pygame.image.load('pictures/m_Hit small.png'),
#                                     (small_xy_hit_size, small_xy_hit_size))
# game_display.blit(empty_cell, (180, display_size_y / 3))
#
# padded_cell = pygame.transform.scale(pygame.image.load('pictures/m_Miss small.png'),
#                                      (small_xy_hit_size, small_xy_hit_size))
# game_display.blit(padded_cell, (200, display_size_y / 3))


# Параметры поля
pygame.draw.rect(game_display, (215, 215, 215),
                 (display_size_x / 2.3, display_size_y / 10, display_size_x / 2, display_size_x / 2))
pygame.draw.rect(game_display, (250, 203, 3),
                 (display_size_x / 2.3, display_size_y / 10, display_size_x / 2, display_size_x / 2), 3)


def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()


while True:
    event_handler()
    pygame.display.update()
