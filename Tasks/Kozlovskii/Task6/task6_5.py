def f(n):
    if n <= 0:
        print("Значение должно быть больше 0!")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)
n = int(input('Введите порядковый номер элемента: '))
print('Элемент: ', f(n))