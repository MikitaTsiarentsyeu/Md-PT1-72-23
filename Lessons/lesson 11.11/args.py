def test_func(a:int, b:list):
    print(id(a), id(b))
    a += 2
    b[0] += 2
    print(id(a), id(b))

test_int = 3
test_list = [3]

print(id(test_int), id(test_list))
test_func(test_int, test_list)
print(id(test_int), id(test_list))

def pos(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")

pos(2, -5, "test")
# pos(2, -5, "test", 6) error
# pos() error

pos(b=4, c="si", a=0)
pos(10, 4, "si")

def oper(a, b, sign='+', console=True):
    res = None
    if sign == "+":
        res = a+b
    elif sign == "*":
        res = a*b
    elif sign == "-":
        res = a-b
    elif sign == "/":
        res = a/b

    if console:
        print(res)

    return res
    
oper(2, 3, "*")
oper(2, 3, console=False)


def add_elem(elem, l=[]):
    l.append(elem)
    return l

print(add_elem(1))
print(add_elem(2))

print(1,2,3,4,5,6,7,8,9,10)

def sum(*numbers):
    print(type(numbers))
    res = 0
    for i in numbers:
        res += i
    return res

print(sum(1,2,3,4,5))

def sum(*numbers, console=True):
    if console:
        print(type(numbers))
    res = 0
    for i in numbers:
        res += i
    return res

print(sum(1,2,3,4,5,console=True))

l = [1,2,3,4,5]
print(sum(*l))

def my_print(*args, **kwargs):
    print(*args, sep=kwargs['sep'], end=kwargs['end'])

my_print(1,2,3,4,5,6,7,8,9, sep=',', end='.')