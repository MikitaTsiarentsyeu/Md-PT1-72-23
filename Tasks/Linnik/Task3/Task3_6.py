# 6. Write a program that takes a string as input and returns the string with all vowels removed.
string = input()
vowels = ('a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U')
for i in range(len(string)):
    if string[i] not in vowels:
        print(string[i], end='')


