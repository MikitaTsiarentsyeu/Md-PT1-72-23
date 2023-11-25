'''5. Write a function that takes an ordered list of numbers
without duplicates and returns a string with ranges for those numbers, check the example below:
get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
get_ranges([4,7,10])  -> "4, 7, 10"
get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"'''

list = [0, 1, 2, 3, 4, 7, 8, 10]
list2 = [4,7,10]
list3 = [2, 3, 8, 9]
list4 = [25 ,26, 27, 28]

def get_ranges(lst):
    begin = lst[0]
    result = []

    for i in range(len(lst) - 1):
        if lst[i] + 1 == lst[i + 1]:
            continue
        else:
            if begin == lst[i]:
                result.append(f'{lst[i]}')
            else:
                result.append(f'{begin}-{lst[i]}')
            begin = lst[i + 1]

    if lst[-2] + 1 == lst[-1]:
        result.append(f'{begin}-{lst[-1]}')
    else:
        result.append(f'{lst[-1]}')
    return (', '.join(result))

print(get_ranges(list))
print(get_ranges(list2))
print(get_ranges(list3))
print(get_ranges(list4))


