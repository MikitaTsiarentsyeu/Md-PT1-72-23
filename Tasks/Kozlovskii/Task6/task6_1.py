s = input('Введите строку:')

def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]

print(reverse(s))