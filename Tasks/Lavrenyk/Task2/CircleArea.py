from math import pi

while True:
    try:
        radius = float(input('Введите радиус круга: '))
    except ValueError:
        print('Ошибка! Введено неверное значение, повторите ввод!\n')
        continue
    break

print(f'Площадь круга: {pi * radius * radius}')