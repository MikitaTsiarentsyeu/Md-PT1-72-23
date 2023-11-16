"""Модуль содержит в себе функцию, предназначенную для подсчёта 
количества буквенных символов в строке, находящихся в нижнем и
верхнем регистрах."""


def case_counter(string: str) -> tuple:
    """Принимает в качестве аргумента строку.

    Возвращает 2 числа: количество буквенных символов в строке, 
    находящихся в нижнем и верхнем регистрах соответственно.

    Ввод аргументов, отличных от озвученных типов, - может привести к 
    неккоректной работе функции."""

    low = 0
    up = 0

    for char in string:
        if char.islower():
            low += 1
        elif char.isupper():
            up += 1

    return low, up
