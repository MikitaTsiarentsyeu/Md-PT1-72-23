# Write a function that takes a string as an argument and returns two numbers, first for count of lower case letters, second for count of the upper case letters in the initial string.

def low_upp_case(some_str):
    upp = 0
    low = 0
    new_str = some_str.replace(" ", "")
    for i in new_str:
        if i.isupper():
            upp += 1
        else:
            low += 1
    
    return f"Count of lower case letters is {low}\nCount of the upper case letters is {upp}"
        


print(low_upp_case(input(("Enter string list:\n"))))
