"""Модуль предназначен для подсчёта гласных букв в строке, введённой 
пользователем с клавиатуры.

Язык ввода - английский."""


INTRO = """Добро пожаловать в программу для подсчёта гласных букв в 
строках.

Данная программа позволяет вам ввести любую строку на английском языке, 
после чего на экране отобразится количество гласных букв, 
присутствующих в ней.
Обращайте внимание на язык ввода, ибо если в строке будут отсутствовать 
гласные, присутствующие в английском алфавите, - результатом будет "0".

Для остановки программы введите "0" вместо запрашиваемой строки и 
нажмите клавишу "Enter".
"""


def main():
    '''Содержит в себе основную логику модуля и выполняет её, если модуль
    запущен самостоятельно, а не как встраиваемый.'''

    print(INTRO)

    users_str = input('Введите строку на английском языке и нажмите клавишу \
"Enter":\n')

    while users_str != "0":
        counter = 0

        for _ in users_str:
            if _ in [
                'A',
                'a',
                'E',
                'e',
                'I',
                'i',
                'O',
                'o',
                'U',
                'u',
                'Y',
                'y',
            ]:
                counter += 1

        print(f'Количество гласных букв в введённой строке: {counter}.')

        users_str = input('Введите следующую строку на английском языке и \
нажмите клавишу "Enter":\n')

    print('\nВсего доброго.')


if __name__ == '__main__':
    main()