def to_next_hour(hhmm, next='we_need'):
    ''' Данная функция создана для уменьшения объёма словаря и перехода к следующему через уже знакомы числа. '''
    if next == 'we_need':
        if hhmm[0]+1 > 12:
            hhmm[0] = hhmm[0]+1 - 12
        else:
            hhmm[0] = hhmm[0] + 1
        return hhmm[0]
    else:
        if hh_mm[0] > 12:
            hh_mm[0] = hh_mm[0] - 12
        return hhmm[0]


numbers = {
    0: [''],
    1: ['', "первого"],
    2: ["два", "второго"],
    3: ["три", "третьего"],
    4: ["четыре", "четвёртого"],
    5: ["пять", "пятого"],
    6: ["шесть", "шестого"],
    7: ["семь", "седьмого"],
    8: ["восемь", "восьмого"],
    9: ["девять", "девятого"],
    10: ["десять", "десятого"],
    11: ["одиннадцать", "одиннадцатого"],
    12: ["двенадцать", "двенадцатого"],
    13: ["тринадцать"],
    14: ["четырнадцать"],
    15: ["пятнадцать"],
    16: ["шестнадцать"],
    17: ["семнадцать"],
    18: ["восемнадцать"],
    19: ["девятнадцать"],
    20: ["двадцать"],
}

print("Введите время в виде чч:мм")
user_time = f"{input('Который час? ')}:{input('Сколько минут? ')}"

hh_mm = user_time.split(':')
hh_mm[0] = int(hh_mm[0])
hh_mm[1] = int(hh_mm[1])

if len(user_time) > 5 or hh_mm[0] > 24 or hh_mm[1] > 59:
    print("Напишите правильно время")

# :} min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
elif hh_mm[1] == 0:
    hh_mm[0] = to_next_hour(hh_mm, 'no')
    if hh_mm[0] == 0 and hh_mm[1] == 0:
        print("Час ночи у вас")
    elif hh_mm[0] == 1:
        print(f'{user_time} - один час ровно')
    elif hh_mm[0] in [2, 3, 4]:
        print(f'{user_time} - {numbers[hh_mm[0]][0]} часа ровно')
    else:
        print(f'{user_time} - {numbers[hh_mm[0]][0]} часов ровно')

# :} min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
elif hh_mm[1] < 30:
    hh_mm[0] = to_next_hour(hh_mm)
    if hh_mm[1] == 1:
        print(f'{user_time} - одна минута {numbers[hh_mm[0]][1]}')
    elif hh_mm[1] == 2:
        print(f'{user_time} - две минуты {numbers[hh_mm[0]][1]}')
    elif hh_mm[1] in [3, 4]:
        print(f'{user_time} - {numbers[hh_mm[1]][0]} минуты {numbers[hh_mm[0]][1]}')
    elif hh_mm[1] in range(5, 21):
        print(f'{user_time} - {numbers[hh_mm[1]][0]} минут {numbers[hh_mm[0]][1]}')
    elif hh_mm[1] == 21:
        print(f'{user_time} - двадцать одна минута {numbers[hh_mm[0]][1]}')
    elif hh_mm[1] in range(22, 25):
        print(f'{user_time} - двадцать {"две" if hh_mm[1] == 22 else numbers[int(str(hh_mm[1])[-1])][0]} минуты {numbers[hh_mm[0]][1]}')
    elif hh_mm[1] in range(25, 30):
        print(f'{user_time} - двадцать {numbers[int(str(hh_mm[1])[-1])][0]} минут {numbers[hh_mm[0]][1]}')

# :} min == 30: половина такого-то (15:30 - половина четвёртого)
elif hh_mm[1] == 30:
    hh_mm[0] = to_next_hour(hh_mm)
    print(f'{user_time} - половина {numbers[hh_mm[0]][1]}')

# min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
elif 30 < hh_mm[1] < 45:
    hh_mm[0] = to_next_hour(hh_mm)
    if hh_mm[1] < 40:
        print(f'{user_time} - тридцать {numbers[int(str(hh_mm[1])[-1])][0]} минут {numbers[hh_mm[0]][1]}')
    else:
        print(f'{user_time} - сорок {numbers[int(str(hh_mm[1])[-1])][0]} минут {numbers[hh_mm[0]][1]}')

# min >= 45 без min такого-то (08:54 - без шести минут девять)
elif hh_mm[1] >= 45:
    print(f'{user_time} - ')
