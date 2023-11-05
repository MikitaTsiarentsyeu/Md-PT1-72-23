"""Модуль предназначен для нахождения самого большого простого числа 
из всех чисел, введённых пользователем с клавиатуры."""


INTRO = """Добро пожаловать в программу для нахождения самого большого 
простого числа (из введённых с клавиатуры).

Данная программа позволяет вам ввести любое количество натуральных 
чисел (целых положительных) через запятую, после чего программа 
отыщет среди них самое большое простое число.
Обращаю ваше внимание, что число является целым, если его десятичное 
представление не содержит дробной части, соответственно, ввод целого 
числа в формате "1.0" и т. п. будет воспринят программой как ошибочный.

Для остановки программы введите "q" вместо запрашиваемой строки и 
нажмите клавишу "Enter".
"""


def main():
    '''Содержит в себе основную логику модуля и выполняет её, если модуль
    запущен самостоятельно, а не как встраиваемый.'''

    print(INTRO)

    users_str = input('Введите натуральные числа через запятую и нажмите \
клавишу "Enter":\n')

    while users_str != "q":
        list_of_numbers = []
        not_primes = []

        for _ in users_str.split(','):
            if _.strip().isdecimal():
                if int(_.strip()) >= 0:
                    list_of_numbers.append(int(_.strip()))
                else:
                    print(f'Введённые вами данные ({_.strip()}) некорректны. \
Повторите ввод заново.')

                    break
            else:
                print(f'Введённые вами данные ({_.strip()}) некорректны. \
Повторите ввод заново.')

                break

        if len(list_of_numbers) != 0:
            try:
                for _ in list_of_numbers:
                    for div in range(2, int(_**0.5) + 1):
                        if _ % div == 0:
                            not_primes.append(_)

                            break

                answer = max(
                    set(list_of_numbers).symmetric_difference(set(not_primes))
                )

                if answer == 0 or answer == 1:
                    print("Натуральное число является простым, если оно \
отлично от 0 и 1 и единственными его делителями являются только оно само и \
единица.")
                else:
                    print(f"Самое большое простое число из представленных: \
{answer}.")
            except:
                print('Все представленные числа оказались составными.')

        users_str = input('Введите натуральные числа через запятую и нажмите \
клавишу "Enter":\n')

    print('\nВсего доброго.')


if __name__ == '__main__':
    main()
