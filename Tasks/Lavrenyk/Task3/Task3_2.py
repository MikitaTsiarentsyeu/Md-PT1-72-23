from re import findall

user_input = input('Enter the numbers separated by a space: ')
numbers = list(map(int, findall('-?\d+', user_input)))

print(sum([i for i in numbers if i % 2 == 0]))