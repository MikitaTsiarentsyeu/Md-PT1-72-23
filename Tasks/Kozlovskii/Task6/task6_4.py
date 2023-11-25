def f(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * f(a, b - 1))
a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат:", f(a, b))