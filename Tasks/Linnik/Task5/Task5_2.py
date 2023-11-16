def reverse_words_in_list(list_str: list) -> list:
    """
    Return a new list of strings that are all reversed.
    :parameter list_str: list.
    :return: list.
    """
    new_list = []
    for i in list_str:
        string = ''
        for j in range(len(i)-1, -1, -1):
            string += i[j]
        new_list.append(string)

    return new_list


print(reverse_words_in_list(['wow', 'Linnik', 'Zarina']))
print(reverse_words_in_list(['did', 'lentiv', 'bomb']))
print(reverse_words_in_list(['a', 'AcdB', 'gorilla']))
print(reverse_words_in_list(['a']))
print(reverse_words_in_list([]))
