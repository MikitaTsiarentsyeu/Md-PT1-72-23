n = int(input('Enter any index of element from Fibonacci sequence: '))
def get_number(n):
    '''this function returns the value from the Fibonacci sequence by its index'''
    if n <= 1:
        return n
    else:
        return get_number(n-1) + get_number(n-2)
print(get_number(n))