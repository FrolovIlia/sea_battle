import json

with open('data_file.json') as f:
    ships_dict = json.load(f)


def stop_game(counter=None):
    if counter == len(ships_dict["layout"]):
        print('Игра закончена! Поздравляю!')
        return True
    else:
        return False


shot = [0, 0]


def shooting(shoot):
    counter = 0
    hit = [int(shoot[0]), int(shoot[1])]
    for i in ships_dict["layout"]:
        if hit in i['positions']:
            print(i['positions'])
            print("Попадание")
            print(f"Удаляем из списка {hit}")
            i['positions'].remove(hit)
            if len(i['positions']) == 0:
                print("Корабль полностью подбит")
                counter += 1
                return counter

        else:
            print(i['positions'])
            print("Нет попадания")
        print()

# print(ships_dict["layout"])
