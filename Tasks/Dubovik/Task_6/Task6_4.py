def power(a, b):
    if b != 0:
        return a * power(a, b - 1)
    else:
        return 1

a = 2
b = 3
print(power(a, b))