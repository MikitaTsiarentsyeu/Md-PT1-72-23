string = input()
def reverse_string(string):  
    ''' с каждым новым вызовом самой себя, функция начинает чтение строки с первого символа, добавляя нулевой в конец'''  
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]
print(reverse_string(string))