from random import randint

while True:
    try:
        a = int(input('Введите начальное значение диапазона: '))
        b = int(input('Введите конечное значение диапазона:  '))
    except ValueError:
        print('Ошибка в одном из значений! Повторите ввод!\n')
        continue
    break

rand = randint(a, b)
print(f'Выпавшее случайное число: {rand}')
