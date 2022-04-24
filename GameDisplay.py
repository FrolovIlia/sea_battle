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
game_display.blit(sign_counter, (115, 80)
                  )
player_name = hit_counter_1.render('Player 1', True, (180, 0, 0))
game_display.blit(player_name, (75, 140))

pygame.draw.line(game_display, 'black', [70, 120], [170, 120], 2)

# Параметры кораблей и вспомогательных элементов
carrier_shape = pygame.transform.scale(pygame.image.load('pictures/Carrier_shape.png'), (120, 40))
game_display.blit(carrier_shape, (display_size_x / 14, 200))

# empty_cell = pygame.transform.scale(pygame.image.load('pictures/m_Hit small.png'),
#                                     (small_xy_hit_size, small_xy_hit_size))
# game_display.blit(empty_cell, (180, display_size_y / 3))
#
# padded_cell = pygame.transform.scale(pygame.image.load('pictures/m_Miss small.png'),
#                                      (small_xy_hit_size, small_xy_hit_size))
# game_display.blit(padded_cell, (200, display_size_y / 3))

battleship_shape = pygame.transform.scale(pygame.image.load('pictures/Battleship_Shape.png'), (120, 40))
game_display.blit(battleship_shape, (display_size_x / 14, 250))

cruiser_shape = pygame.transform.scale(pygame.image.load('pictures/Cruiser_Shape.png'), (120, 40))
game_display.blit(cruiser_shape, (display_size_x / 14, 300))

submarine_shape = pygame.transform.scale(pygame.image.load('pictures/Submarine_Shape.png'), (120, 40))
game_display.blit(submarine_shape, (display_size_x / 14, 350))

destroyer_shape = pygame.transform.scale(pygame.image.load('pictures/Destroyer_Shape.png'), (120, 40))
game_display.blit(destroyer_shape, (display_size_x / 14, 400))

# Параметры поля.
# Создаём новый дисплей, для игрового поля.

field_surf = pygame.Surface((display_size_x / 2, display_size_x / 2))
field_surf.fill("gray")

# Разбиваем поле линиями
lines = 10


def draw_lines():
    for line in range(1, lines):
        pygame.draw.line(field_surf, (0, 0, 0), ((field_surf.get_width() / lines) * line, 0),
                         ((field_surf.get_width() / lines) * line, field_surf.get_width()), 2)

        pygame.draw.line(field_surf, (0, 0, 0), (0, (field_surf.get_height() / lines) * line),
                         (field_surf.get_height(), (field_surf.get_height() / lines) * line), 2)


draw_lines()

field_frame = pygame.draw.rect(field_surf, (250, 203, 3),
                               (0, 0, display_size_x / 2, display_size_x / 2), 3)

game_display.blit(field_surf, (display_size_x / 2.3, display_size_y / 10))

#
#


# События поля
LEFT = 1
RIGHT = 3
running = 1


def click_on_field():
    if (display_size_x / 2.3) < pygame.mouse.get_pos()[0] < ((display_size_x / 2.3) + (display_size_x / 2)) and (
            display_size_y / 10) < pygame.mouse.get_pos()[1] < ((display_size_y / 10) + display_size_x / 2):
        return True


def convert_to_cell(field_pos):  # Принимает координаты внутри игрового поля.
    cell_size = (field_surf.get_width() / 10, field_surf.get_height() / 10)
    field_cell = (int(field_pos[0] // cell_size[0]), int(field_pos[1] // cell_size[1]))
    return field_cell


while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEBUTTONDOWN and (event.button == LEFT or event.button == RIGHT) and click_on_field():
        print("Нажата кнопка мыши")
        field_pos_correction = (int(pygame.mouse.get_pos()[0] - display_size_x / 2.3),
                                int(pygame.mouse.get_pos()[1] - display_size_y / 10))
        print(f"По координатам: {pygame.mouse.get_pos()}")
        print(f"Координаты внутри поля: {field_pos_correction}")
        print(f"Координаты ячейки: {convert_to_cell(field_pos_correction)}")

    pygame.display.flip()


# Условия выхода и основной цикл
def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()


while True:
    event_handler()
    pygame.display.update()
