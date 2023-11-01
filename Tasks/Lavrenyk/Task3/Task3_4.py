from re import findall


def find_second_large(lst: list) -> float:
    """
    Algorithm that find the second-largest number in the list
    """
    max_list = [min(numbers)] * 2
    for i in numbers:
        if i > max_list[0]:
            max_list[1] = max_list[0]
            max_list[0] = i
            continue
        if i > max_list[1] and i != max_list[0]:
            max_list[1] = i

    return max_list[1]


while True:
    user_input = input('Enter the numbers separated by a space: ')

    numbers = list(map(float, findall(r'[-+]?\d*\.*\d+', user_input)))
    if numbers:
        break

print(find_second_large(numbers))

