# a program that takes a list of numbers as input and returns the sum of all even numbers in the list.

numbers = list(range(11)) # to simplify program testing, the list was created automatically
total = 0
for i in numbers:
    if numbers[i] % 2 == 0:
        total += numbers[i]
print(f'The sum of all even numbers in the list equal {total}')