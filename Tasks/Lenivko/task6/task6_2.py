string = input()
def is_palindrom(value):
    if len(value) == 0:
        return ('this is palindrom')
    else:
        if value[0] == value[-1]:
            return is_palindrom(value[1:-1])
        else:
            return 'this is not palindrom'
    
print(is_palindrom(string))