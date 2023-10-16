from bs4 import BeautifulSoup
from urllib.request import urlopen
from decimal import Decimal


def getUSD():
    return float(BeautifulSoup(urlopen('https://kurs.onliner.by/'))
                 .find_all('p', {'class': 'value'})[2]
                 .text
                 .split()[0]
                 .replace(',', '.'))


if __name__ == '__main__':
    while True:
        try:
            usd = Decimal(input('Введите количество USD для обмена: '))
        except ValueError:
            print('Ошибка! Введены неверные данные, попробуйте еще раз!\n')
            continue
        break

    print(f'BYN: {usd * Decimal(f"{getUSD()}")}')
