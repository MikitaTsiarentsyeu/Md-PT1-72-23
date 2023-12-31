"""Модуль предназначен для нахождения второго по величине значения, 
введённого пользователем с клавиатуры."""


INTRO = """Добро пожаловать в программу для нахождения второго по 
величине введённого значения.

Данная программа позволяет вам ввести любое количество чисел через 
запятую, после чего программа отыщет второе по величине значение и 
выведет его на экран.

Для остановки программы введите "q" вместо запрашиваемой строки и 
нажмите клавишу "Enter".
"""


def main():
    '''Содержит в себе основную логику модуля и выполняет её, если модуль
    запущен самостоятельно, а не как встраиваемый.'''

    print(INTRO)

    users_str = input('Введите числа через запятую и нажмите клавишу \
"Enter":\n')

    while users_str != "q":
        list_of_numbers = []

        for _ in users_str.split(','):
            try:
                list_of_numbers.append(float(_.strip()))
            except:
                print(f'Введённые вами данные ({_.strip()}) некорректны. \
Повторите ввод заново.')

                break
        else:
            if len(list_of_numbers) >= 2:
                while len(list_of_numbers) != 0:
                    max_elem = max(list_of_numbers)

                    list_of_numbers.remove(max_elem)

                    if max_elem in list_of_numbers:
                        continue
                    else:
                        if len(list_of_numbers) != 0:
                            print(f'Второе по величине значение: \
{max(list_of_numbers)}.')

                            break
                else:
                    print('Введённые вами числа одинаковы. Повторите ввод.')
            else:
                print('Вами введено только одно число. Повторите ввод.')

        users_str = input('Введите числа через запятую и нажмите клавишу \
"Enter":\n')

    print('\nВсего доброго.')


if __name__ == '__main__':
    main()
