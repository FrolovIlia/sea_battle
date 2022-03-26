import json

with open('data_file.json') as f:
    templates = json.load(f)

print()
print(templates['shipTypes']['carrier'])
print()
print(templates['layout'])
print()



