
def start_field():
    field_size = 10
    field_condition = [['~'] * field_size for i in range(field_size)]
    return field_condition


def show_field(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()


show_field(start_field())

print('Добро пожаловать в игру "Морской Бой!"')
print('Пришло время первого выстрела...')

shot = input('Введите координаты в формате "xy": ')

