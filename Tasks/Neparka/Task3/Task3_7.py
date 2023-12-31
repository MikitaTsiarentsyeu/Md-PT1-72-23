"""Модуль предназначен для редактирования введённой пользователем 
строки путём замены регистров символов."""


INTRO = """Добро пожаловать в программу по замене регистров вводимых 
символов.

Данная программа позволяет вам ввести любую строку, а взамен получить 
новую, в которой символы с нижним регистром заменены на символы с 
верхним и наоборот.

Для остановки программы введите "0" вместо запрашиваемой строки и 
нажмите клавишу "Enter".
"""


def main():
    '''Содержит в себе основную логику модуля и выполняет её, если модуль
    запущен самостоятельно, а не как встраиваемый.'''

    print(INTRO)

    users_str = input('Введите строку и нажмите клавишу "Enter":\n')

    while users_str != "0":
        print(users_str.swapcase())

        users_str = input('Введите следующую строку и нажмите клавишу \
"Enter":\n')

    print('\nВсего доброго.')


if __name__ == '__main__':
    main()
