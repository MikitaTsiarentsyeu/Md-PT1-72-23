'''3. Write a function that takes a list of strings as an argument
and returns a new list with all the strings that have a length greater than 5.'''
l = ["My", "name", "is", "Alexey", "Wordmorethan5letters"]
l2 = []
def func(l):
    for i in l:
        if len(i) > 5:
            l2.append(i)
    return l2
print(func(l))