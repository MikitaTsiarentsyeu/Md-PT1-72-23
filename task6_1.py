def reverse(string):
    # perhaps, the line is null
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
string = ('yellow, green, red')
print(reverse(string))