"""Модуль предназначен для подсчёта площади круга по введённому с клавиатуры 
радиусу данного круга."""


from math import pi


INTRO = """Добро пожаловать в программу по вычислению площади круга по его 
радиусу.
Точность вычисленного значения - три знака после запятой. Учитывайте это при
задании значений для расчёта.

Для остановки программы введите "q" вместо запрашиваемого значения и нажмите 
клавишу "Enter".
----------------------------------------------------------------------------
"""


def circle_area_with_r(r) -> float:
    '''Предназначена для нахождения значения площади круга по радиусу.'''

    return pi * r**2


def main():
    '''Содержит в себе основную логику модуля и выполняет её, если модуль
    запущен самостоятельно, а не как встраиваемый.'''

    print(INTRO)

    value = input('Введите радиус круга и нажмите клавишу "Enter": ')

    while value != "q":
        try:
            if float(value) > 0:
                print(f'Площадь круга равна \
{round(circle_area_with_r(float(value)), 3)}')
            else:
                print(f'Введённое вами значение ({value}) некорректно для \
вычисления площади круга. Повторите ввод.')
        except:
            print(f'Введённое вами значение ({value}) некорректно. \
Повторите ввод.')

        value = input('Введите радиус круга и нажмите клавишу "Enter": ')

    print('\nВсего доброго.')


if __name__ == '__main__':
    main()
