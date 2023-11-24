'''4. Write a function that takes a string as an argument and returns two numbers,
first for count of lower case letters, second for count of the upper case letters in the initial string.
'''
str = "AAAooooouuuIIII"
str2 = "4. Write a function that takes a string as an argument and returns two numbers,first for count of lower case letters, second for count of the upper case letters in the initial string."
def upper_lower(str):
    upper = 0
    lower = 0
    for i in str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return (f'Uppercase letters:{upper},Lowercase letters: {lower}')
print(upper_lower(str))
print(upper_lower(str2))

