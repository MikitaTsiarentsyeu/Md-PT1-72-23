while True:
    try:
        kps = float(input('Введите скорость (км/час): '))
    except ValueError:
        print('Ошибка! Введены неверные данные, повторите ввод!\n')
        continue
    break

print(f'Метры в секунду: {kps / 3.6}')