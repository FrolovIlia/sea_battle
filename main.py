import Ships
from Ships import *


def start_field():
    field_size = 10
    clean_field = [['~'] * field_size for _ in range(field_size)]
    return clean_field


field_condition = start_field()


def show_field(a: list):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()


def add_ships(base_field: list):
    all_pos = []
    for i in Ships.ships_dict['layout']:
        all_pos.extend(i['positions'])

    for x, y in all_pos:
        base_field[x][y] = 's'
    return base_field


def check_shoot(shoot):
    if len(shoot) == 2 and shoot.isnumeric():
        print('Данные верны')
        return shot
    else:
        trying = input('Пожалуйста, введите корректные координаты в формате XY: ')
        check_shoot(trying)


show_field(start_field())

print('Добро пожаловать в игру "Морской Бой!"')
print('Выберите координаты от 0 до 9 по X и Y')
print()

while stop_game() is False:
    shot = input('Введите координаты в формате XY: ')
    check_shoot(shot)

    Ships.shooting(shot)
else:
    print("Game Over")
