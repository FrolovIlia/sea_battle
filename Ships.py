import json
from main import shot

with open('data_file.json') as f:
    ships_dict = json.load(f)


for i in ships_dict["layout"]:
    if shot in i['positions']:
        print(i['positions'])
        print("Попадание")
        print(f"Удаляем из списка {shot}")
        i['positions'].remove(shot)
        if len(i['positions']) == 0:
            print("Корабль полностью подбит")

    else:
        print(i['positions'])
        print("Нет попадания")
    print()

# print(ships_dict["layout"])
