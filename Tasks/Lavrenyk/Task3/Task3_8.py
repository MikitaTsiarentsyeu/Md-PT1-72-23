from re import findall


def average(nums: list) -> float:
    return sum(nums) / len(nums)


while True:
    user_input = input('Enter the numbers separated by a space: ')

    numbers = list(map(float, findall(r'[-+]?\d*\.*\d+', user_input)))
    if numbers:
        break

print(average(numbers))