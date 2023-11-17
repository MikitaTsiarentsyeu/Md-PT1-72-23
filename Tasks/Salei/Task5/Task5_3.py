# Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.

def len_string(list):
    """function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5"""
    new_list = []
    for i in list:
        if len(i) > 5:
            new_list.append(i)
    return new_list


print(len_string(input("Enter string list:\n").split()))