"""Модуль содержит в себе функцию для возведения числа в указанную 
степень."""


def the_power(number, power, first_time=True):
    """Принимает в качестве аргумента число и значение степени, в 
    которое необходимо возвести данное число.

    Возвращает число, возведённое в указанную степень.

    Ввод не числовых аргументов может привести к неккоректной работе 
    функции.

    Данная функция является рекуривной, соответственно, учитывая 
    особенности реализации рекурсии, - присутствует потолок по вводимому
    значению степени."""

    if number == 0:
        return 0
    if power == 0:
        return 1
    elif power > 0:
        if isinstance(power, int):
            return the_power(number, power - 1) * number
        elif number > 0:
            if first_time:
                root = 10 ** len(str(power).split('.')[1])
                power = int(
                    str(power).split('.')[0] + str(power).split('.')[1]
                )
            return (the_power(number, power - 1, False) * number) ** (1 / root)
        elif number < 0:
            return 'Не определяется.'
    else:
        if isinstance(power, int):
            return 1 / (the_power(number, -(power) - 1) * number)
        elif number > 0:
            if first_time:
                root = 10 ** len(str(power).split('.')[1])
                power = int(
                    str(power).split('.')[0] + str(power).split('.')[1]
                )
            return 1 / (
                the_power(number, -(power) - 1, False) * number
            ) ** (1 / root)
        elif number < 0:
            return 'Не определяется.'
