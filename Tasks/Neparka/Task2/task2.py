"""Модуль предназначен для перевода введённого пользователем времени 
в формате чч:мм (ч:мм) в текстовую форму."""


INTRO = """Добро пожаловать в программу для текстового представления 
времени.

Данная программа позволяет вам переводить время из формата "чч:мм" или 
"ч:мм" в текстовую форму.

Для остановки программы введите "q" вместо запрашиваемого значения и нажмите 
клавишу "Enter".
"""


numbers = {
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    30: "тридцать",
    40: "сорок",
    "1go": "первого",
    "2go": "второго",
    "3go": "третьего",
    "4go": "четвёртого",
    "5go": "пятого",
    "6go": "шестого",
    "7go": "седьмого",
    "8go": "восьмого",
    "9go": "девятого",
    "10go": "десятого",
    "11go": "одиннадцатого",
    "12go": "двенадцатого",
    "bez2": "двух",
    "bez3": "трёх",
    "bez4": "четырёх",
    "bez5": "пяти",
    "bez6": "шести",
    "bez7": "семи",
    "bez8": "восьми",
    "bez9": "девяти",
    "bez10": "десяти",
    "bez11": "одиннадцати",
    "bez12": "двенадцати",
    "bez13": "тринадцати",
    "bez14": "четырнадцати",
    "bez15": "пятнадцати",
}


def time_input_checker(time: str) -> bool:
    '''Проверяет адекватность пользовательского ввода.

    Необходимые форматы для ввода - "чч:мм" или "ч:мм" во временных пределах.

    Функция возвращает True, если строка удовлетворяет заданным условиям. В 
    противном случае - None.'''

    if len(time) == 5 or len(time) == 4:
        try:
            if time.split(':')[0] != "-0" \
                    and int(time.split(':')[0]) in range(0, 24):
                if time.split(':')[1] != "-0" \
                        and int(time.split(':')[1]) in range(0, 60):
                    return True
                else:
                    print(f'Введённые вами данные ({time}) некорректны. \
Повторите ввод.')
            else:
                print(f'Введённые вами данные ({time}) некорректны. Повторите \
ввод.')
        except:
            print(f'Введённые вами данные ({time}) некорректны. Повторите \
ввод.')
    else:
        print(f'Введённые вами данные ({time}) некорректны. Повторите ввод.')


def hours_to_12(time: str) -> int:
    '''Переводит часы из строки "чч:мм" ("ч:мм") из 24-часового 
    формата в 12-часовой'''

    if int(time.split(':')[0]) > 12:
        return int(time.split(':')[0]) - 12
    return int(time.split(':')[0])


def minutes_splitter(time: str) -> tuple:
    '''Разделяет минуты на десятки и единицы. 

    Ответ представляет в виде списка, где на 0 позиции находятся 
    десятки минут, а на 1 - единицы мнут.'''

    return (int(time.split(':')[1]) // 10 * 10, int(time.split(':')[1]) % 10)


def main():
    '''Содержит в себе основную логику модуля и выполняет её, если модуль
    запущен самостоятельно, а не как встраиваемый.'''

    print(INTRO)

    time_input = input('Введите интересующее вас время в формате "чч:мм" или \
"ч:мм" и нажмите клавишу "Enter": ')

    while time_input != "q":
        if time_input_checker(time_input):
            hours = hours_to_12(time_input)

            if int(time_input.split(':')[1]) == 0:
                if hours == 0:
                    print(f'{time_input} - полночь')
                elif hours == 12:
                    print(f'{time_input} - полдень')
                elif hours == 1:
                    print(f'{time_input} - один час ровно')
                elif hours in (2, 3, 4):
                    print(f'{time_input} - {numbers.get(hours)} часа ровно')
                elif hours in range(5, 12):
                    print(f'{time_input} - {numbers.get(hours)} часов ровно')
            elif int(time_input.split(':')[1]) == 30:
                print(f'{time_input} - половина \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
            elif int(time_input.split(':')[1]) in range(1, 30) \
                    or int(time_input.split(':')[1]) in range(31, 45):
                if minutes_splitter(time_input)[0] == 0:
                    if minutes_splitter(time_input)[1] == 1:
                        print(f'{time_input} - одна минута \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
                    elif minutes_splitter(time_input)[1] == 2:
                        print(f'{time_input} - две минуты \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
                    elif minutes_splitter(time_input)[1] in (3, 4):
                        print(f'{time_input} - \
{numbers.get(minutes_splitter(time_input)[1])} минуты \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
                    else:
                        print(f'{time_input} - \
{numbers.get(minutes_splitter(time_input)[1])} минут \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
                elif minutes_splitter(time_input)[1] == 0:
                    print(f'{time_input} - \
{numbers.get(minutes_splitter(time_input)[0])} минут \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
                else:
                    if int(time_input.split(':')[1]) in range(11, 20):
                        print(f'{time_input} - \
{numbers.get(int(time_input.split(':')[1]))} минут \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
                    else:
                        if minutes_splitter(time_input)[1] == 1:
                            print(f'{time_input} - \
{numbers.get(minutes_splitter(time_input)[0])} \
одна минута \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
                        elif minutes_splitter(time_input)[1] == 2:
                            print(f'{time_input} - \
{numbers.get(minutes_splitter(time_input)[0])} \
две минуты \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
                        elif minutes_splitter(time_input)[1] in (3, 4):
                            print(f'{time_input} - \
{numbers.get(minutes_splitter(time_input)[0])} \
{numbers.get(minutes_splitter(time_input)[1])} минуты \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
                        else:
                            print(f'{time_input} - \
{numbers.get(minutes_splitter(time_input)[0])} \
{numbers.get(minutes_splitter(time_input)[1], '')} минут \
{numbers.get(f"{hours + 1 if hours != 12 else 1}go")}')
            else:
                if int(time_input.split(':')[1]) == 59:
                    if hours in (0, 12):
                        print(f'{time_input} - без одной минуты час')
                    else:
                        print(f'{time_input} - без одной минуты \
{numbers.get(hours + 1)}')
                else:
                    if hours in (0, 12):
                        print(f'{time_input} - без \
{numbers.get(f"bez{60 - int(time_input.split(':')[1])}")} минут час')
                    else:
                        print(f'{time_input} - без \
{numbers.get(f"bez{60 - int(time_input.split(':')[1])}")} минут \
{numbers.get(hours + 1)}')

        time_input = input('Введите интересующее вас время в формате "чч:мм" \
или "ч:мм" и нажмите клавишу "Enter": ')

    print('\nВсего доброго.')


if __name__ == '__main__':
    main()
