import json

with open('data_file.json') as f:
    templates = json.load(f)

print(templates)
print()
print(templates['shipTypes'])
print()
print(templates['layout'])
