"""Модуль содержит в себе функцию, предназначенную для проверки строки 
на то, является ли она палиндромом или нет."""


def is_a_palindrome(string: str, first_time=True) -> bool:
    """Принимает в качестве аргумента строку.

    Возвращает True в том случае, если строка является палиндромом. 
    Иначе - False.

    Ввод аргумента, отличного от типа "str", - может привести к 
    неккоректной работе функции.

    Иногда палиндромом называют любой симметричный набор символов, 
    однако обращаем ваше внимание, что данная программа заточена, в 
    основном, на работу с буквенными и цифровыми символами. Все знаки 
    препинания игнорируются программой для корректной работы с 
    текстовыми строками. Учитывайте это при вводе исходных данных.

    Ввод пустой строки, или же строки, содержащий один символ, - 
    даст в результате False, ибо по определению палиндромом является 
    сочетание символов."""

    if first_time:
        if string.isspace() or len(string) <= 1:
            return False

        for _ in [
            ' ',
            '.',
            '?',
            '!',
            ',',
            ';',
            ':',
            '-',
            '—',
            '(',
            ')',
            '"',
            '\'',
            '’',
            '«',
            '»',
        ]:
            string = string.replace(_, '')

        if len(string) <= 1:
            return False

        string = string.lower()

    if len(string) >= 2:
        if string[0] == string[len(string)-1]:
            string = string[1:-1]
            return is_a_palindrome(string, False)
        return False
    return True
