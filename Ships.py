import json

dead_ships = 0

with open('data_file.json') as f:
    ships_dict = json.load(f)

def stop_game():
    if dead_ships == len(ships_dict["layout"]):
        print('Игра закончена! Поздравляю!')
        return True
    else:
        return False


def shooting(shoot):
    global dead_ships
    hit = [int(shoot[0]), int(shoot[1])]
    for ship in ships_dict["layout"]:
        if hit in ship['positions']:
            print(ship['positions'])
            print("Попадание")
            print(f"Удаляем из списка {hit}")
            ship['positions'].remove(hit)
            if len(ship['positions']) == 0:
                print("Корабль полностью подбит")
                dead_ships += 1


        else:
            print(ship['positions'])
            print("Нет попадания")
        print()

