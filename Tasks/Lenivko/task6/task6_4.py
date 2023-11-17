num = int(input('Enter a number: '))
power = int(input('Enter a power of number: '))

def get_power(num, power):
    ''' this function returns the power of given number'''
    if power == 0:
        return 1
    elif power == 1:
        return num
    else:
        return num * get_power(num, power-1)
print(get_power(num, power))
    