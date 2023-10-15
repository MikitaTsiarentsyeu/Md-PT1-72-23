while True:
    try:
        Celsius = float(input('Введите градусы Цельсия: '))
    except ValueError:
        print('Ошибка! Нужно ввести одно единственное число!\n')
        continue
    break

print(f'Полученные градусы по Фаренгейту: {9 / 5 * Celsius + 32}')
