"""Модуль предназначен для перевода долларов в белорусские рубли по 
актуальному курсу.

Курс для конвертации берётся с популярного портала "onliner.by".

Значение для конвертации вводится пользователем с клавиатуры."""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import decimal


INTRO = """Добро пожаловать в программу по конвертации валюты.

Данная программа позволяет вам переводить доллары в белорусские рубли по 
актуальному на момент использования курсу.
Курс валюты поставляется популярным порталом "onliner.by".

Для остановки программы введите "q" вместо запрашиваемого значения и нажмите 
клавишу "Enter".
----------------------------------------------------------------------------
Пожалуйста, ожидайте. Программа загружает актуальный курс валюты.
"""


def main():
    '''Содержит в себе основную логику модуля и выполняет её, если модуль
    запущен самостоятельно, а не как встраиваемый.'''

    print(INTRO)

    response = urlopen("https://kurs.onliner.by/")

    soup = BeautifulSoup(response, features="lxml")
    tags = soup.find_all('p', {'class': "value"})

    value = input('Введите количество долларов для конвертации и нажмите \
клавишу "Enter": ')

    while value != "q":
        try:
            if float(value) >= 0:
                byn = decimal.Decimal(value) * decimal.Decimal(
                    tags[1].text.replace(",", ".").rstrip("BYN"))
                print(f'{byn} белорусских рублей.')
            else:
                print(f'Введённое вами значение ({value}) некорректно для \
конвертации. Повторите ввод.')
        except:
            print(f'Введённое вами значение ({value}) некорректно. \
Повторите ввод.')

        value = input('Введите количество долларов для конвертации и нажмите \
клавишу "Enter": ')

    print('\nВсего доброго.')


if __name__ == '__main__':
    main()
