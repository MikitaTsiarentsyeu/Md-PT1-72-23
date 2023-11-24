n = 15
def func(n):
    if n <= 1:
        return n
    return func(n - 1) + func(n - 2)
print(func(n))

