import json

with open('data_file.json') as f:
    templates = json.load(f)

# print()
# print(templates['shipTypes']['carrier'])
# print()
# print(templates['layout'])
# print()

for i in templates['layout']:
    print(f"Корабль {i['ship']} на позиции {i['positions']}")

