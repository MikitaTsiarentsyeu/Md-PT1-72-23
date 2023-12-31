"""Модуль содержит в себе функцию, предназначенную для подсчёта 
количества появлений заданного символа в строке."""


def count_of_occurrences(string: str, character: str, count=0) -> int:
    """Принимает в качестве аргументов строку и символ, число появлений 
    которого необходимо отыскать в данной строке.

    Возвращает число появений заданного символа.

    Ввод аргументов, отличных от озвученных типов, - может привести к 
    неккоректной работе функции."""

    if string.find(character) == -1:
        return count
    return count_of_occurrences(
        string[string.find(character)+1:], character, count+1
    )
