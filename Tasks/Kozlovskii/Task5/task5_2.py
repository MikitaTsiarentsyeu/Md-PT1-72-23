a = input('Введите данные:')
def f(a):
    b = a.split()
    res = [i[::-1] for i in b]
    return res
print(f(a))