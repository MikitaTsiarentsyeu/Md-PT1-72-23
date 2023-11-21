"""Модуль содержит в себе функцию, возвращающее указанное по счёту 
число из последовательности Фибоначчи."""


def number_in_the_fibonacci(number: int, nth=2, left_num=0, right_num=1) -> int:
    """Принимает в качестве аргумента число.

    Возвращает число из послеовательности Фибоначчи, стоящее на 
    указанной позиции.

    Ввод аргументов, отличных от озвученных правил, - может привести к 
    неккоректной работе функции."""

    if number == 1:
        return left_num
    elif number == 2:
        return right_num
    elif number != nth:
        return number_in_the_fibonacci(number, nth+1, right_num, left_num+right_num)
    return right_num
