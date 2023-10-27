my_time = input('Enter the time in format hh:mm: ').split(':')
my_time_int = list(map(int,my_time))

print(my_time)
print(my_time_int)

d_hour = {1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять',6:'шесть', 7:'семь', 8:'восемь', 9:'девять', 10:'десять',
        11:'одиннадцать', 12:' двенадцать'}


for key in d_hour:
      if my_time_int[0] == key and my_time_int[1] == 0 and my_time_int[0] < 5:
       print(d_hour.get(key), 'часа ровно')
      elif my_time_int[0] == key and my_time_int[1] == 0 and  my_time_int[0] > 4:
       print(d_hour.get(key), 'часов ровно')

if my_time_int[1] == 30 and my_time_int[0] == 0:
    print('половина первого')
elif my_time_int[1] == 30 and my_time_int[0] == 1:
    print('половина второго')
elif my_time_int[1] == 30 and my_time_int[0] ==2:
    print('половина третьего')
elif my_time_int[1] == 30 and my_time_int[0] == 3:
    print('половина четвёртого')
elif my_time_int[1] == 30 and my_time_int[0] == 4:
    print('половина пятого')
elif my_time_int[1] == 30 and my_time_int[0] == 5:
    print('половина шестого')
elif my_time_int[1] == 30 and my_time_int[0] == 6:
    print('половина седьмого')
elif my_time_int[1] == 30 and my_time_int[0] == 7:
    print('половина восьмого')
elif my_time_int[1] == 30 and my_time_int[0] == 8:
    print('половина девятого')
elif my_time_int[1] == 30 and my_time_int[0] == 9:
    print('половина десятого')
elif my_time_int[1] == 30 and my_time_int[0] == 10:
    print('половина одиннадцатого')
elif my_time_int[1] == 30 and my_time_int[0] == 11:
    print('половина двенадцатого')
elif my_time_int[1] == 30 and my_time_int[0] == 12:
    print('половина первого')

for key in d_hour:
    if my_time_int[1] < 45 and my_time_int[1] !=30 and my_time_int[0] != 1 and my_time_int[0] != 0 \
            and my_time_int[0] <5 and my_time_int[0] == key:
        print(d_hour.get(key), 'часа', my_time_int[1], 'минут')
    elif my_time_int[1] < 45 and my_time_int[1] !=30 and my_time_int[0] == 1:
        print('1 час',my_time_int[1], 'минут')
    elif my_time_int[1] < 45 and my_time_int[1] !=30 and my_time_int[0] != 1  and my_time_int[0] > 4 and my_time_int[0] < 13\
            and my_time_int[0] == key:
        print(d_hour.get(key), 'часов', my_time_int[1], 'минут')
    elif my_time_int[1] == 45 and my_time_int[0] == key:
        print('Без пятнадцати',d_hour.get(key + 1))
    elif my_time_int[1] == 46 and my_time_int[0] == key:
        print('Без четырнадцати',d_hour.get(key + 1))
    elif my_time_int[1] == 47 and my_time_int[0] == key:
        print('Без тринадцати',d_hour.get(key + 1))
    elif my_time_int[1] == 48 and my_time_int[0] == key:
        print('Без двенадцати',d_hour.get(key + 1))
    elif my_time_int[1] == 49 and my_time_int[0] == key:
        print('Без одиннадцати',d_hour.get(key + 1))
    elif my_time_int[1] == 50 and my_time_int[0] == key:
        print('Без десяти',d_hour.get(key + 1))
    elif my_time_int[1] == 51 and my_time_int[0] == key:
        print('Без девяти',d_hour.get(key + 1))
    elif my_time_int[1] == 52 and my_time_int[0] == key:
        print('Без восьми',d_hour.get(key + 1))
    elif my_time_int[1] == 53 and my_time_int[0] == key:
        print('Без семи',d_hour.get(key + 1))
    elif my_time_int[1] == 54 and my_time_int[0] == key:
        print('Без шести',d_hour.get(key + 1))
    elif my_time_int[1] == 55 and my_time_int[0] == key:
        print('Без пяти',d_hour.get(key + 1))
    elif my_time_int[1] == 56 and my_time_int[0] == key:
        print('Без четырёх',d_hour.get(key + 1))
    elif my_time_int[1] == 57 and my_time_int[0] == key:
        print('Без трёх',d_hour.get(key + 1))
    elif my_time_int[1] == 58 and my_time_int[0] == key:
        print('Без двух',d_hour.get(key + 1))
    elif my_time_int[1] == 59 and my_time_int[0] == key:
        print('Без одной',d_hour.get(key + 1))







