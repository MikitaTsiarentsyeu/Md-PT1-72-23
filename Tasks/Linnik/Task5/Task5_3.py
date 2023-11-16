def find_strings_greater5(list_str: list) -> list:
    """
    Return a new list with all the strings that have a length greater than 5.
    :parameter list_str: list.
    :return: list.
    """
    new_list = []
    for i in list_str:
        if len(i) > 5:
            new_list.append(i)
    return new_list


print(find_strings_greater5([]))
print(find_strings_greater5(['a']))
print(find_strings_greater5(['wow', 'Linnik', 'Zarina']))
print(find_strings_greater5(['did', 'lentiv', 'bomb']))
print(find_strings_greater5(['a', 'AcdB', 'gorilla']))

