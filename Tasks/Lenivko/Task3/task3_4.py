# This program takes a list of numbers as input and returns the second largest number in the list.


numbers = list(range(11)) # to simplify program testing, the list was created automatically
#numbers = [1, 4 , 6, 10, 25, 100, 36, 11, 46, 56, 101]
max_1 = min(numbers)
max_2 = 0
for i in range(len(numbers)):
    if numbers[i] > max_1:
        max_2 = max_1
        max_1 = numbers[i]
        if max_2 < numbers[i] > max_1:
            max_2 = numbers[i]
print(max_2)