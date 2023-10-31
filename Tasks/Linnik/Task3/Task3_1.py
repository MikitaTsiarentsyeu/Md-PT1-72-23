# 1. Write a program that takes a string as input from a user and returns the number of vowels in the string.
string = input()
counter = 0
for i in string:
    if i in ('a', 'e', 'o', 'i', 'u'):  # Use a tuple because size of a tuple is less than a list has
        counter += 1
print(counter)
