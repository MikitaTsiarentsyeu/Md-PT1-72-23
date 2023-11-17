symb = input('Add any symbol:')
string = input('Enter a string:' )

def count_occurences(string, symb, counter = 0):
    if len(string) < 1:
        return counter
    if string[0] == symb:
        counter += 1
    return count_occurences(string[1:], symb, counter)

print(count_occurences(string, symb))