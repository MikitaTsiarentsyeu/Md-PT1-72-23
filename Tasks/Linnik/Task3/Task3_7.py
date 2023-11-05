# 7. Write a program that takes a string as input
# returns the string with all capital letters converted to lowercase and vice versa.

string = "vEry ImPortAnT thinG ToDaY? yEs/NO."
uppercase_letters = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
)
lowercase_letters = tuple([i.lower() for i in uppercase_letters])

for i in string:
    if i in uppercase_letters:
        print(lowercase_letters[uppercase_letters.index(i)], end='')
    elif i in lowercase_letters:
        print(uppercase_letters[lowercase_letters.index(i)], end='')
    else:
        print(i, end='')
