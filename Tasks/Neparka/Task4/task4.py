"""Модуль предназначен для выравнивания текста, расположенного в файле 
"text.txt", находящегося в той же директории, что и данный модуль, по 
ширине, соответствующей заданному пользователем с клавиатуры количеству
символов в строке.

Результат работы программы сводится в новый файл, находящийся в той же
директории, что и данный модуль.
Название нового файла: "aligned_to_(количество символов числом).txt"."""


import os


INTRO = """Добро пожаловать в программу для форматирования текста по 
ширине.

Программа работает с текстом, находящимся в файле "text.txt",
который необходимо расположить в той же директории (папке), где 
находится и сама программа. Поместите файл, содержащий текст для 
редактирования, в корректное место, а также проверьте правильность его 
названия и его расширение.

Данная программа запрашивает у вас количество символов для задания 
ширины, по которой и будет происходить выравнивание. Нижний порог 
ввода - 36 символов (ширина итогового текста должна быть больше 35 
символов).
Обращаю ваше внимание, что количество символов является целым числом,  
т. е. его десятичное представление не содержит дробной части, 
соответственно, ввод целого числа в формате "1.0" и т. п. будет 
воспринят программой как ошибочный.

Результом работы программы является новый файл, находящийся в той же
директории, где и исходный файл.
Название нового файла: "aligned_to_(количество символов числом).txt".
Обращаю ваше внимание, что если на момент работы программы в директории 
уже присутствует файл с аналогичным названием, - он будет заменён на 
новый.

Для остановки программы введите "q" вместо запрашиваемой строки и 
нажмите клавишу "Enter".
"""


def spacemaker(string_to_modify: str, width: int) -> str:
    """Поочерёдно добавляет необходимое количество пробелов в 
    представленную строку до достижения требуемой ширины."""

    spaces_delta = 1

    string_to_modify = string_to_modify.strip()

    while len(string_to_modify) != width:
        spaces_delta += 1

        space_pos = string_to_modify.find(' ')

        if space_pos != -1:
            while len(string_to_modify) != width:
                if space_pos != -1:
                    string_to_modify = f"\
{string_to_modify[:space_pos]} {string_to_modify[space_pos:]}"

                    space_pos = string_to_modify.find(
                        ' ',
                        space_pos + spaces_delta,
                    )
                else:
                    break
        else:
            return string_to_modify

    return string_to_modify


def main():
    '''Содержит в себе основную логику модуля и выполняет её, если 
    модуль запущен самостоятельно, а не как встраиваемый.'''

    print(INTRO)

    aligned_to = input('Введите количество символов в строке и нажмите \
клавишу "Enter": ')

    while aligned_to != "q":
        if aligned_to.isdecimal():
            if int(aligned_to) > 35:
                if os.path.exists(f"aligned_to_{aligned_to}.txt"):
                    os.remove(f"aligned_to_{aligned_to}.txt")

                try:
                    with open(file='text.txt', encoding='UTF-8') as text:
                        string = text.read(int(aligned_to)-1)
                        next_string = text.read(int(aligned_to)-1)

                        with open(
                            f"aligned_to_{aligned_to}.txt",
                            "a",
                            encoding='UTF-8',
                        ) as result:
                            while string:
                                if len(string) > int(aligned_to)-1:
                                    string, next_string \
                                        = string[:int(aligned_to)-1], \
                                        f"\
{string[int(aligned_to)-1:]}{next_string}"

                                if string.partition('\n')[1] == '':
                                    if len(string) == int(aligned_to)-1:
                                        if next_string.startswith(" "):
                                            print(string, file=result)

                                            string, next_string \
                                                = next_string.lstrip(), \
                                                text.read(int(aligned_to)-1)

                                            continue
                                        else:
                                            print(
                                                spacemaker(
                                                    string.rpartition(" ")[0],
                                                    int(aligned_to)-1,
                                                ),
                                                file=result,
                                            )

                                            string, next_string \
                                                = f'\
{string.rpartition(" ")[2]}{next_string}', text.read(int(aligned_to)-1)

                                            continue
                                    if len(string) < int(aligned_to)-1:
                                        if next_string != '':
                                            how_long = spacemaker(
                                                string,
                                                int(aligned_to)-1,
                                            )

                                            if len(how_long) \
                                                    == int(aligned_to)-1:
                                                print(
                                                    how_long,
                                                    file=result,
                                                )

                                                string, next_string = \
                                                    next_string.lstrip(

                                                    ), text.read(
                                                        int(aligned_to)-1
                                                    )

                                                continue
                                            else:
                                                string, next_string \
                                                    = f"\
{string}{next_string}".lstrip(), text.read(int(aligned_to)-1)
                                        else:
                                            print(
                                                string,
                                                file=result,
                                            )

                                            break

                                else:
                                    print(
                                        string.partition('\n')[
                                            0
                                        ].lstrip(),
                                        file=result,
                                    )

                                    string, next_string \
                                        = f"\
{string.partition('\n')[2]}{next_string}", text.read(int(aligned_to)-1)

                    if os.path.exists(f"aligned_to_{aligned_to}.txt"):
                        print(f'\nФайл "aligned_to_{aligned_to}.txt" успешно \
создан.\n')
                    else:
                        print('Представленный вами файл пуст. Заполните его \
текстом для редактирования.')
                except:
                    print('Файл с текстом на редактирование не найден. \
Проверьте его наличие, а также правильность его названия и расширение.')
            else:
                print(f'Введённые вами данные ({aligned_to}) некорректны. \
Повторите ввод заново.')
        else:
            print(f'Введённые вами данные ({aligned_to}) некорректны. \
Повторите ввод заново.')

        aligned_to = input('Введите количество символов в строке и нажмите \
клавишу "Enter":\n')

    print('\nВсего доброго.')


if __name__ == '__main__':
    main()
