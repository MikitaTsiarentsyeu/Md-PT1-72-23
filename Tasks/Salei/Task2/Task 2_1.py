

d_hour = {
    0:  ["двенадцать", "первого", "час"],
    1:  ["один", "второго", "два"],
    2:  ["два", "третьего", "три"],
    3:  ["три", "четвертого", "четыре"],
    4:  ["четыре", "пятого", "пять"],
    5:  ["пять", "шестого", "шесть"],
    6:  ["шесть", "седьмого", "семь"],
    7:  ["семь", "восьмого", "восемь"],
    8:  ["восемь", "девятого", "девять"],
    9:  ["девять", "десятого", "десять"],
    10: ["десять", "одиннадцатого", "одинадцать"],
    11: ["одиннадцать", "двенадцатого", "двенадцать"],
    12: ["двенадцать", "первого", "час"],
}


d_minutes = {
    0:  ["ровно"],
    1:  ["одна минута"],
    2:  ["две минуты"],
    3:  ["три минуты"],
    4:  ["четыре минуты"],
    5:  ["пять минут"],
    6:  ["шесть минут"],
    7:  ["семь минут"],
    8:  ["восемь минут"],
    9:  ["девять минут"],
    10: ["десять минут"],
    11: ["одиннадцать минут"],
    12: ["двенадцать минут"],
    13: ["тринадцать минут"],
    14: ["четырнадцать минут"],
    15: ["пятнадцать минут"],
    16: ["шестнадцать минут"],
    17: ["семнадцать минут"],
    18: ["восемнадцать минут"],
    19: ["девятнадцать минут"],
    20: ["двадцать минут"],
    21: ["двадцать одна минута"],
    22: ["двадцать две минуты"],
    23: ["двадцать три минуты"],
    24: ["двадцать четыре минуты"],
    25: ["двадцать пять минут"],
    26: ["двадцать шесть минут"],
    27: ["двадцать семь минут"],
    28: ["двадцать восемь минут"],
    29: ["двадцать девять минут"],
    30: ["половина"],
    31: ["тридцать одна минута"],
    32: ["тридцать две минуты"],
    33: ["тридцать три минуты"],
    34: ["тридцать четыре минуты"],
    35: ["тридцать пять минут"],
    36: ["тридцать шесть минут"],
    37: ["тридцать семь минут"],
    38: ["тридцать восемь минут"],
    39: ["тридцать девять минут"],
    40: ["сорок минут"],
    41: ["сорок одна минута"],
    42: ["сорок две минуты"],
    43: ["сорок три минуты"],
    44: ["сорок четыре минуты"],
    45: ["без пятнадцати"],
    46: ["без четырнадцати минут"],
    47: ["без тринадцати минут"],
    48: ["без двенадцати минут"],
    49: ["без одинадцати минут"],
    50: ["без десяти"],
    51: ["без девяти минут"],
    52: ["без восьми минут"],
    53: ["без семи минут"],
    54: ["без шести минут"],
    55: ["без пяти"],
    56: ["без четырех минут"],
    57: ["без трех минут"],
    58: ["без двух минут"],
    59: ["без одной минуты"]
}


i_time = input("Введите время в формате 'HH:mm': ")
time_split = i_time.split(":")
hour = int(time_split[0])
min = int(time_split[1])

if hour > 12:
    hour = hour - 12

res_hour = d_hour.get(hour)
res_minutes = d_minutes.get(min)

if hour == 12 and min == 0:
    print("ровно полдень")
elif 1 < hour < 12 and min == 0:
    if hour in range(2, 4):
        x = "часа"
    elif hour == 1:
        x = "час"
    else:
        x = "часов"
    res_current_time = f"{res_hour[0]} {x} ровно"
    print(res_current_time)
else:
    print("ровно полночь")

if min == 30:
    res_current_time = f"{res_minutes[0]} {res_hour[1]}"
    print(res_current_time)

if 0 < min < 30 or 30 < min < 45:
    res_current_time = f"{res_minutes[0]} {res_hour[1]}"
    print(res_current_time)

if min > 44:
    res_current_time = f"{res_minutes[0]} {res_hour[2]}"
    print(res_current_time)