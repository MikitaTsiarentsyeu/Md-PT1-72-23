from num2words import num2words as n2


class formats:
    NUM_ORD_PREFIXES = {1: 'одн', 2: 'дв', 3: 'тр', 4: 'четыр',
                         5: 'пят', 6: 'шест', 7: 'сем', 8: 'вос',
                         9: 'девят', 10: 'десят', 11: 'одиннадцат', 12: 'двенадцат',
                         13: 'тринадцат', 14: 'четырнадцат', 15: 'пятнадцат'}

    NUM_POSTFIXES = {1: ('а', 'ой'), 2: ('е', 'ух'), 3: ('и', 'ёх'), 4: ('е', 'ёх'),
                      5: ('ь', 'и'), 6: ('ь', 'и'), 7: ('ь', 'и'), 8: ('емь', 'ьми'),
                      9: ('ь', 'и'), 10: ('ь', 'и'), 11: ('ь', 'и'), 12: ('ь', 'и'),
                      13: ('ь', 'и'), 14: ('ь', 'и'), 15: ('ь', 'и')}

    WORD_HOURS = {
        '01': ['час', 'первого'],
        '02': ['два', 'второго'],
        '03': ['три', 'третьего'],
        '04': ['четыре', 'четвертого'],
        '05': ['пять', 'пятого'],
        '06': ['шесть', 'шестого'],
        '07': ['семь', 'седьмого'],
        '08': ['восемь', 'восмого'],
        '09': ['девять', 'девятого'],
        '10': ['десять', 'десятого'],
        '11': ['одиннадцать', 'одиннадцатого'],
        '12': ['двенадцать', 'двенацатого']
    }

    UNUSUAL = {
        21: 'двадцать одна',
        22: 'двадцать две',
        31: 'тридцать одна',
        32: 'тридцать две',
        41: 'сорок одна',
        42: 'сорок две',
    }

    def get_hour(self, h: str, n: int):
        if h not in self.WORD_HOURS:
            return self.WORD_HOURS['01'][n]
        return self.WORD_HOURS[h][n]

    def get_below_half(self, n: int, below: bool = True) -> str:
        if n not in self.NUM_ORD_PREFIXES and n not in [21, 22, 31, 32, 41, 42]:
            return n2(n, lang='ru')
        elif n in [21, 22, 31, 32, 41, 42]:
            return self.UNUSUAL[n]
        else:
            return [f'{self.NUM_ORD_PREFIXES[n]}{self.NUM_POSTFIXES[n][1]}',
                    f'{self.NUM_ORD_PREFIXES[n]}{self.NUM_POSTFIXES[n][0]}'][below]

    @staticmethod
    def get_mins_postfix(m, below = True):
        if m in [1, 21, 31, 41] and below == True:
            MINS_POSTFIXES = 'а'
        elif ((m in range(2, 5) and below == True)
              or m in range(22, 25)
              or m in range (32, 35)
              or m in range(42, 45)
              or (m == 1 and below == False)):
            MINS_POSTFIXES = 'ы'
        else:
            MINS_POSTFIXES = ''

        return f'минут{MINS_POSTFIXES}'

    @staticmethod
    def get_hour_postfix(h):
        if 1 < h <= 4:
            HOUR_POSTFIXES = 'а'
        else:
            HOUR_POSTFIXES = 'ов'

        return f'час{HOUR_POSTFIXES} '

    @staticmethod
    def zerofill(s: str, lenght) -> str:
        return str(abs(int(s) - 12)).zfill(lenght)

    def output_time(self, lst_time: list) -> None:
        hours = lst_time[0] \
            if lst_time[0] in self.WORD_HOURS \
            else self.zerofill(lst_time[0], 2)
        mins = int(lst_time[1])
        choosing = None

        if mins == 0:
            choosing = (f'{self.WORD_HOURS[hours][0]} '
                          f'{["", self.get_hour_postfix(int(hours))][int(hours) > 1]}'
                          f'ровно')
        elif 0 < mins < 30 or 30 < mins < 45:
            choosing = (f'{self.get_below_half(mins)} '
                                f'{self.get_mins_postfix(mins)} '
                                f'{self.get_hour(str(int(hours) + 1).zfill(2), 1)}')
        elif mins == 30:
            choosing = f'половина {self.get_hour(str(int(hours) + 1).zfill(2), 1)}'
        elif mins >= 45:
            choosing = (f'без {self.get_below_half(60 - mins, False)} '
                        f'{self.get_mins_postfix(60 - mins, False)} '
                        f'{self.get_hour(str(int(hours) + 1).zfill(2), 0)}')

        print(choosing)

def test_num(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    time_lst = None
    formats = formats()
    while True:
        user_input = input('Введите время в формате hh:mm ')
        if (len(user_input) == 5
                and user_input[2] == ':'
                and test_num(user_input[:2])
                and 0 <= int(user_input[:2]) <= 24
                and test_num(user_input[-2:])
                and 0 <= int(user_input[-2:]) <= 59):
            time_lst = user_input.split(':')
            break
        else:
            print('Ошибка ввода, проверьте введенные данные и повторите попытку!\n')

    formats.output_time(time_lst)