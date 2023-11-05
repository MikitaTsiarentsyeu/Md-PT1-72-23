# 2. Write a program that takes a list of numbers as input a
# returns the sum of all even numbers in the list.
string_of_numbers = input('Enter your numbers in this string: ')
list_of_numbers = [int(i) for i in string_of_numbers.split()]
sum_even = 0
for i in list_of_numbers:
    if i % 2 == 0:
        sum_even += i
print(sum_even)
