

def outer():

    def inner():
        print("hello from inner func")

    return inner

test_func = outer()
print(test_func)
test_func()

outer()()

def operator(op):

    if op == '+':
        def operation(a, b):
            return a+b
    elif op == '-':
        def operation(a, b):
            return a-b
    elif op == '*':
        def operation(a, b):
            return a*b
    elif op == '/':
        def operation(a, b):
            return a/b
        
    return operation
    
mult = operator('*')
print(mult(2, 3))

print(operator('+')(2, 3))

def operator(op):

    def operation(a, b):
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        elif op == '*':
            return a*b
        elif op == '/':
            return a/b
        
    return operation

mult = operator('*')
print(mult(2, 3))

print(operator('+')(2, 3))


def power_of(n):
    def inner(i):
        return i**n
    
    return inner

square = power_of(2)
cube = power_of(3)

print(square(4), cube(2))

def counter(n=0):
    def inner():
        nonlocal n
        n += 1
        return n
    
    return inner

counter_from_10 = counter(10)
print(counter_from_10())
print(counter_from_10())
print(counter_from_10())

counter_from_100 = counter(100)
print(counter_from_100())
print(counter_from_100())
print(counter_from_100())

print(counter_from_10())
print(counter_from_10())
print(counter_from_10())
