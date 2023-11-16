'''2. Write a function that takes a
list of strings as an argument and returns a new list of
strings that are all reversed.'''
str = ["My", "name", "is", "Alex"]

def rev_str(str):
    str2 = str[::-1]
    return str2

print(rev_str(str))

