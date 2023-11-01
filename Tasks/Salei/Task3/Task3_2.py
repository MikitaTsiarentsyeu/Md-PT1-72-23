# Write a program that takes a list of numbers as input and returns
# the sum of all even numbers in the list.

numbers_list = [16, 146, 11, 108, 399, 512, 1005, 22, 1137]
even_numbers_sum = 0
for i in numbers_list:
    if i % 2 == 0:
        even_numbers_sum+=i
print(f"Sum of all even number is {even_numbers_sum}")