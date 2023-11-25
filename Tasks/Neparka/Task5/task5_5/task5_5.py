"""Модуль содержит в себе функцию, предназначенную для нахождения 
последовательностей чисел в списке."""


def get_ranges(list_of_numbers: list) -> str:
    """Принимает в качестве аргумента упорядоченный по возрастанию 
    список чисел без дубликатов.

    Возвращает строку, перечисляющую последовательности присутсвующих 
    чисел.

    Ввод аргументов, отличных от озвученных правил, - может привести к 
    неккоректной работе функции."""

    ranges = []
    first_part_of_final_string = ''
    final_string = ''

    for pos in range(len(list_of_numbers)):
        if first_part_of_final_string == '':
            first_part_of_final_string = f'{list_of_numbers[pos]}'
            final_string = first_part_of_final_string

        if pos != len(list_of_numbers) - 1:
            if list_of_numbers[pos] + 1 != list_of_numbers[pos+1]:
                ranges.append(f'{final_string}')
                first_part_of_final_string = ''
                final_string = ''
            else:
                final_string = f'\
{first_part_of_final_string}-{list_of_numbers[pos+1]}'
        else:
            if list_of_numbers[pos-1] != list_of_numbers[pos] - 1:
                ranges.append(f'{list_of_numbers[pos]}')
            else:
                ranges.append(
                    f'{first_part_of_final_string}-{list_of_numbers[pos]}'
                )

    return ', '.join(ranges)
