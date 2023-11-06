# 1. Write a program that takes a string as input from a user and returns the number of vowels in the string.
string = input()
vowels = ('a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U')
# Use a tuple because size of a tuple is less than a list has
counter = 0
for i in string:
    if i in vowels:
        counter += 1
print(counter)
