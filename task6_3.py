def count_of_char(string, char):
    # perhaps, the line is null
    if len(string) == 0:
        return 0
    # if the 1 item == our char
    elif string[0] == char:
        # [1:] - go to the right of the 1 (second) item
        return 1 + count_of_char(string[1:], char)
    else:
        return count_of_char(string[1:], char)
#string for input: (yellow, green, red)
string = input("Enter the string:")
search_char = 'e'
print("Quantity of chars:")
print(count_of_char(string, search_char))