a = input('Введите значения:')
def f(a):
    b = a.split()
    line = []
    for i in b:
        if len(i) > 5:
            line.append(i)
    return  line
print(f(a))
