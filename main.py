import GameLogic
from GameLogic import *


def start_field():
    field_size = 10
    clean_field = [['~'] * field_size for _ in range(field_size)]
    return clean_field


def show_field(field: list):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end=' ')
        print()


def add_ships(base_field: list):
    all_pos = []
    for ship in GameLogic.ships_dict['layout']:
        all_pos.extend(ship['positions'])

    new_field = [line.copy() for line in base_field]
    for x, y in all_pos:
        new_field[x][y] = 's'
    return new_field


def check_shoot(shoot: str) -> list[int]:
    if len(shoot) == 2 and shoot.isnumeric():
        print('Данные верны')
        return [int(shoot[0]), int(shoot[1])]
    else:
        trying = input('Пожалуйста, введите корректные координаты в формате XY: ')
        return check_shoot(trying)


def note_shoot(user_field: list[list], test_field: list[list], shoot: list):
    x, y = shoot
    if test_field[x][y] == 's':
        user_field[x][y] = '*'
    else:
        user_field[x][y] = 'x'

    return user_field


if __name__ == '__main__':
    field_condition = start_field()
    show_field(field_condition)

    print('Добро пожаловать в игру "Морской Бой!"')
    print('Выберите координаты от 0 до 9 по X и Y')
    print()

    field_with_ships = add_ships(field_condition)
    show_field(field_with_ships)

    while stop_game() is False:
        shot = input('Введите координаты в формате XY: ')
        shot = check_shoot(shot)

        GameLogic.shooting(shot)
        # перерисовка поля по новым данным словаря позиций кораблей.
        field_condition = note_shoot(field_condition, field_with_ships, shot)
        show_field(field_condition)


    else:
        print("Game Over")
